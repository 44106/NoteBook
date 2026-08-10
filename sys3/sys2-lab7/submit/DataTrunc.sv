`include "core_struct.vh"

module DataTrunc (
    input CorePack::data_t dmem_rdata,
    input CorePack::mem_op_enum mem_op,
    input CorePack::addr_t dmem_raddr,
    output CorePack::data_t read_data
);

  import CorePack::*;

    logic [2:0] offset=dmem_raddr[2:0]; 
    logic [63:0]shifted_data;            
    logic [7:0]byte_val;              
    logic [15:0]half_val;               
    logic [31:0]word_val;             
 
always_comb begin
   byte_val=8'b0;
   half_val=16'b0;
   word_val=32'b0;
   shifted_data=dmem_rdata>>(offset * 8);
        case (mem_op)
            MEM_UB: begin
                byte_val=shifted_data[7:0];
                read_data={56'b0,byte_val};
            end
            MEM_UH: begin  
                half_val=shifted_data[15:0];
                read_data={48'b0,half_val};
            end
            MEM_UW: begin
                word_val=shifted_data[31:0];
                read_data={32'b0,word_val};
            end
            MEM_B: begin 
                byte_val=shifted_data[7:0];
                read_data={{56{byte_val[7]}},byte_val};
            end
            MEM_H: begin 
                half_val=shifted_data[15:0];
                read_data={{48{half_val[15]}},half_val};
            end
            MEM_W: begin
                word_val=shifted_data[31:0];
                read_data={{32{word_val[31]}},word_val};
            end
            MEM_D: read_data=dmem_rdata; 
            default:read_data=64'b0;    
        endcase
    end
   

  // Data trunction
  // fill your code

endmodule
