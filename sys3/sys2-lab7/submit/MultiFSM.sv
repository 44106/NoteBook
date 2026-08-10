`include "mem_ift.vh" 

module MultiFSM(
    input logic clk,
    input logic rst,
    Mem_ift.Master imem_ift,
    Mem_ift.Master dmem_ift,
    input  logic we_mem,
    input  logic re_mem,
    output logic stall
);

    typedef enum logic [2:0] {
        IDLE,  IF1,  IF2,  WAITFOR2,  MEM1,  MEM2
    } MultiFSM_state;

    MultiFSM_state current_state;
    MultiFSM_state next_state;

    always_ff @(posedge rst or posedge clk) begin
        if (rst) current_state <= IF1;
        else     current_state <= next_state;
    end

    always_comb begin
        next_state=current_state;
        case (current_state)
            IDLE: next_state=IF1;
            IF1: begin
                if(imem_ift.r_request_valid && imem_ift.r_request_ready)begin
                    if(re_mem || we_mem)begin
                        next_state=WAITFOR2;
                    end else begin
                        next_state=IF2;
                    end
                end
            end
            IF2: begin
                if(imem_ift.r_reply_valid && imem_ift.r_reply_ready)begin
                    next_state=IDLE;
                end
            end
            WAITFOR2: begin
                if(imem_ift.r_reply_valid && imem_ift.r_reply_ready)begin
                    next_state=MEM1;
                end
            end
            MEM1: begin
                if(we_mem)begin
                    if(dmem_ift.w_request_valid && dmem_ift.w_request_ready)begin
                        next_state=MEM2;
                    end
                end else begin
                    if(dmem_ift.r_request_valid && dmem_ift.r_request_ready)begin
                        next_state=MEM2;
                    end
                end
            end
            MEM2: begin
                if(we_mem)begin
                    if(dmem_ift.w_reply_valid && dmem_ift.w_reply_ready)begin
                        next_state=IDLE;
                    end
                end else begin
                    if(dmem_ift.r_reply_valid && dmem_ift.r_reply_ready)begin
                        next_state=IDLE;
                    end
                end
            end
            default: next_state=IDLE;
        endcase
    end

    always_comb begin
        stall=1'b1;
        imem_ift.r_request_valid = 1'b0;
        imem_ift.r_reply_ready   = 1'b0;
        dmem_ift.r_request_valid = 1'b0;
        dmem_ift.w_request_valid = 1'b0;
        dmem_ift.r_reply_ready   = 1'b0;
        dmem_ift.w_reply_ready   = 1'b0;
        case(current_state)
            IDLE: stall=0;
            IF1: imem_ift.r_request_valid=1'b1;
            IF2: imem_ift.r_reply_ready=1'b1;
            WAITFOR2: imem_ift.r_reply_ready=1'b1;
            MEM1: begin
                if(we_mem)begin
                    dmem_ift.w_request_valid=1'b1;
                end else begin
                    dmem_ift.r_request_valid=1'b1;
                end
            end
            MEM2: begin
                if(re_mem)begin
                    dmem_ift.r_reply_ready=1'b1;
                end else begin
                    dmem_ift.w_reply_ready=1'b1;
                end
            end
            default: begin
            end
        endcase
    end
endmodule