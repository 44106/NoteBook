`include "core_struct.vh"
`include "mem_ift.vh"
`include "csr_struct.vh"
module Core (
    input clk,
    input rst,
    input time_int,

    Mem_ift.Master imem_ift,
    Mem_ift.Master dmem_ift,
    output cosim_valid,
    output CorePack::CoreInfo cosim_core_info,
    output CsrPack::CSRPack cosim_csr_info,
    output cosim_interrupt,
    output cosim_switch_mode,
    output CorePack::data_t cosim_cause
);
    import CorePack::*;
    import CsrPack::*;

    addr_t pc, next_pc;
    inst_t inst;
    data_t read_data_1, read_data_2;
    data_t read_data_1_reg, read_data_2_reg;
    data_t imm_value;
    data_t alu_res;
    data_t wb_val;
    data_t temp;
    logic br_taken;
    logic stall;
    logic we_reg;
    logic we_mem;
    logic re_mem;
    logic npc_sel;
    imm_op_enum immgen_op;
    alu_op_enum alu_op;
    cmp_op_enum cmp_op;
    alu_asel_op_enum alu_asel;
    alu_bsel_op_enum alu_bsel;
    wb_sel_op_enum wb_sel;
    mem_op_enum mem_op;
    reg_ind_t rs1;
    reg_ind_t rs2;
    reg_ind_t rd;
    addr_t dmem_addr;
    data_t dmem_wdata;
    mask_t dmem_wmask;
    data_t dmem_rdata;
    logic flush;
    logic load_use_hazard;
    logic fsm_stall;
    logic [1:0] priv;               
    logic switch_mode;              
    data_t pc_csr;                  
    data_t csr_val_id;              
    ExceptPack except_id_out; 
    logic [63:0] csr_zimm_ext;
    logic [63:0] csr_operand;
    logic [63:0] csr_write_res;

    assign rs1 = if_id_reg.inst[19:15];
    assign rs2 = if_id_reg.inst[24:20];
    assign rd  = if_id_reg.inst[11:7];

    typedef enum logic [1:0] {
        SELECT_FROM_EXE,  SELECT_FROM_MEM,  SELECT_FROM_WB,  SELECT_REG
    } forward_sel_op_enum;

    forward_sel_op_enum forwardA_sel;
    forward_sel_op_enum forwardB_sel;

    struct {
      logic valid;
      addr_t pc;
      inst_t inst;
      ExceptPack except;
    }if_id_reg;

    struct {
      logic valid;
      addr_t pc;
      inst_t inst;
      logic npc_sel;
      data_t read_data_1;
      data_t read_data_2;
      data_t read_data_1_reg;
      data_t read_data_2_reg;
      data_t imm_value;
      reg_ind_t rd;
      reg_ind_t rs1;
      reg_ind_t rs2;
      alu_op_enum alu_op;
      cmp_op_enum cmp_op;
      alu_asel_op_enum alu_asel;
      alu_bsel_op_enum alu_bsel;
      wb_sel_op_enum wb_sel;
      mem_op_enum mem_op;
      logic we_reg;
      logic we_mem;
      logic re_mem;
      ExceptPack except; 
      data_t csr_val;
    }id_ex_reg;

    struct {
      logic valid;
      addr_t pc;
      inst_t inst;
      data_t alu_res;
      data_t read_data_1;
      data_t read_data_2;
      reg_ind_t rd;
      reg_ind_t rs1;
      reg_ind_t rs2;
      wb_sel_op_enum wb_sel;
      logic we_reg;
      logic we_mem;
      logic re_mem;
      logic npc_sel;
      mem_op_enum mem_op;
      logic br_taken;
      ExceptPack except;
      data_t csr_val;
      data_t csr_wdata;
    }ex_mem_reg;

    struct{
      logic valid;
      addr_t pc;
      inst_t inst;
      data_t wb_val;
      data_t read_data_1;
      data_t read_data_2;
      data_t alu_res;
      reg_ind_t rd;
      reg_ind_t rs1;
      reg_ind_t rs2;
      logic we_reg;
      logic we_mem;
      logic npc_sel;
      data_t dmem_wdata;
      data_t dmem_rdata;
      logic br_taken;
      ExceptPack except;
      data_t csr_val;
      data_t csr_wdata;
    }mem_wb_reg;

    Controller controller (
        .inst(if_id_reg.inst),
        .we_reg(we_reg),
        .we_mem(we_mem),
        .re_mem(re_mem),
        .npc_sel(npc_sel),
        .immgen_op(immgen_op),
        .alu_op(alu_op),
        .cmp_op(cmp_op),
        .alu_asel(alu_asel),
        .alu_bsel(alu_bsel),
        .wb_sel(wb_sel),
        .mem_op(mem_op)
    );

    RegFile regfile (
        .clk(clk),
        .rst(rst),
        .we(mem_wb_reg.we_reg && mem_wb_reg.valid && !fsm_stall && !cosim_interrupt && !mem_wb_reg.except.except),
        .read_addr_1(rs1),
        .read_addr_2(rs2),
        .write_addr(mem_wb_reg.rd),
        .write_data(mem_wb_reg.wb_val),
        .read_data_1(read_data_1_reg),
        .read_data_2(read_data_2_reg)
    );

    ALU alu (
        .a((id_ex_reg.alu_asel==ASEL_PC)?id_ex_reg.pc:(id_ex_reg.alu_asel==ASEL0)?0:id_ex_reg.read_data_1),
        .b((id_ex_reg.alu_bsel==BSEL_IMM)?id_ex_reg.imm_value:id_ex_reg.read_data_2),
        .alu_op(id_ex_reg.alu_op),
        .res(alu_res)
    );
    assign csr_zimm_ext = {59'b0, id_ex_reg.inst[19:15]};
    assign csr_operand = (id_ex_reg.inst[14]) ? csr_zimm_ext : id_ex_reg.read_data_1;
    always_comb begin
        case (id_ex_reg.inst[13:12])
            2'b01: csr_write_res = csr_operand;
            2'b10: csr_write_res = id_ex_reg.csr_val | csr_operand; 
            2'b11: csr_write_res = id_ex_reg.csr_val & (~csr_operand); 
            default: csr_write_res = csr_operand;
        endcase
    end

    Cmp cmp (
        .a(id_ex_reg.read_data_1),
        .b(id_ex_reg.read_data_2),
        .cmp_op(id_ex_reg.cmp_op),
        .cmp_res(br_taken)
    );

    ImmGen immgen (
        .inst(if_id_reg.inst),
        .imm_op(immgen_op),
        .imm(imm_value)
    );

    DataPkg data_pkg (
        .mem_op(ex_mem_reg.mem_op),
        .reg_data(ex_mem_reg.read_data_2),
        .dmem_waddr(ex_mem_reg.alu_res),
        .dmem_wdata(dmem_wdata)
    );

    DataTrunc data_trunc (
        .dmem_rdata(dmem_rdata),
        .mem_op(ex_mem_reg.mem_op),
        .dmem_raddr(ex_mem_reg.alu_res),
        .read_data(temp)
    );

    MaskGen mask_gen (
        .mem_op(ex_mem_reg.mem_op),
        .dmem_waddr(ex_mem_reg.alu_res),
        .dmem_wmask(dmem_wmask)
    );

    MultiFSM multifsm(
        .clk(clk),
        .rst(rst),
        .imem_ift(imem_ift),
        .dmem_ift(dmem_ift),
        .we_mem(ex_mem_reg.we_mem && ex_mem_reg.valid && !ex_mem_reg.except.except),
        .re_mem(ex_mem_reg.re_mem),
        .stall(fsm_stall)
    );

    IDExceptExamine id_except (
        .clk(clk),
        .rst(rst),
        .stall(fsm_stall), 
        .flush(flush || switch_mode || load_use_hazard), 
        .pc_id(if_id_reg.pc),
        .priv(priv),
        .inst_id(if_id_reg.inst),
        .valid_id(if_id_reg.valid),        
        .except_id(if_id_reg.except),
        .except_exe(except_id_out),
        .except_happen_id()
    );

    assign forwardA_sel=(id_ex_reg.we_reg && (id_ex_reg.rd != 0) && (id_ex_reg.rd == rs1))?SELECT_FROM_EXE:
                        (ex_mem_reg.we_reg && (ex_mem_reg.rd != 0) && (ex_mem_reg.rd == rs1))?SELECT_FROM_MEM:
                        (mem_wb_reg.we_reg && (mem_wb_reg.rd != 0) && (mem_wb_reg.rd == rs1))?SELECT_FROM_WB:SELECT_REG;

    assign forwardB_sel=(id_ex_reg.we_reg && (id_ex_reg.rd != 0) && (id_ex_reg.rd == rs2))?SELECT_FROM_EXE:
                        (ex_mem_reg.we_reg && (ex_mem_reg.rd != 0) && (ex_mem_reg.rd == rs2))?SELECT_FROM_MEM:
                        (mem_wb_reg.we_reg && (mem_wb_reg.rd != 0) && (mem_wb_reg.rd == rs2))?SELECT_FROM_WB:SELECT_REG;

    wire id_is_csr  = (if_id_reg.inst[6:0] == SYSTEM_OPCODE) && (if_id_reg.inst[14:12] != 0) && if_id_reg.valid;
    wire ex_is_csr  = (id_ex_reg.inst[6:0] == SYSTEM_OPCODE) && (id_ex_reg.inst[14:12] != 0) && id_ex_reg.valid;
    wire mem_is_csr = (ex_mem_reg.inst[6:0] == SYSTEM_OPCODE) && (ex_mem_reg.inst[14:12] != 0) && ex_mem_reg.valid;
    wire wb_is_csr  = (mem_wb_reg.inst[6:0] == SYSTEM_OPCODE) && (mem_wb_reg.inst[14:12] != 0) && (mem_wb_reg.valid && !fsm_stall);
    wire csr_hazard = id_is_csr && (ex_is_csr || mem_is_csr || wb_is_csr);

    assign load_use_hazard=(id_ex_reg.re_mem && id_ex_reg.valid && ((id_ex_reg.rd == rs1)||(id_ex_reg.rd == rs2)))||csr_hazard;

    data_t forward_data_exe;
    always_comb begin
        case(id_ex_reg.wb_sel)
            WB_SEL_PC:  forward_data_exe = id_ex_reg.pc + 4; 
            WB_SEL_CSR: forward_data_exe = id_ex_reg.csr_val; 
            default:    forward_data_exe = alu_res;           
        endcase
    end

    always_comb begin
        case (forwardA_sel)
            SELECT_FROM_EXE: read_data_1 = forward_data_exe;
            SELECT_FROM_MEM: read_data_1 = wb_val ;
            SELECT_FROM_WB:  read_data_1 = mem_wb_reg.wb_val;
            SELECT_REG:      read_data_1 = read_data_1_reg;
        endcase
    end

    always_comb begin
        case (forwardB_sel)
            SELECT_FROM_EXE: read_data_2 = forward_data_exe;
            SELECT_FROM_MEM: read_data_2 = wb_val ;
            SELECT_FROM_WB:  read_data_2 = mem_wb_reg.wb_val;
            SELECT_REG:      read_data_2 = read_data_2_reg;
        endcase
    end

    always_ff @(posedge clk or posedge rst) begin
      if (rst) begin
        if_id_reg.valid <= 1'b0;
        id_ex_reg.valid <= 1'b0;
        ex_mem_reg.valid <= 1'b0;
        mem_wb_reg.valid <= 1'b0;
        pc <= 64'b0;
      end else begin
      if (imem_ift.r_reply_valid && imem_ift.r_reply_ready) begin
        inst <= pc[2] ? imem_ift.r_reply_bits.rdata[63:32] : imem_ift.r_reply_bits.rdata[31:0];
      end
      if (dmem_ift.r_reply_valid && dmem_ift.r_reply_ready ) begin
        dmem_rdata <= dmem_ift.r_reply_bits.rdata;
      end if(switch_mode) begin
        if_id_reg.valid <= 0;
        if_id_reg.pc <= 0;
        if_id_reg.inst <= 0;
        if_id_reg.except <= '{default:0};
        pc <= next_pc;

        id_ex_reg.valid <= 0;
        id_ex_reg.inst <= 0;
        id_ex_reg.pc <= 0;
        id_ex_reg.read_data_1 <= 0;
        id_ex_reg.read_data_2 <= 0;
        id_ex_reg.imm_value <= 0;
        id_ex_reg.rd <= 0;
        id_ex_reg.rs1 <= 0;
        id_ex_reg.rs2 <= 0;
        id_ex_reg.npc_sel <= 0;
        id_ex_reg.we_reg <= 0;
        id_ex_reg.we_mem <= 0;
        id_ex_reg.re_mem <= 0;
        id_ex_reg.alu_op <= ALU_DEFAULT;
        id_ex_reg.cmp_op <= CMP_NO;
        id_ex_reg.alu_asel <= ASEL0;
        id_ex_reg.alu_bsel <= BSEL0;
        id_ex_reg.wb_sel <= WB_SEL0;
        id_ex_reg.mem_op <= MEM_NO;
        id_ex_reg.except <= '{default:0};
        id_ex_reg.csr_val <= 0;

        ex_mem_reg.valid <= 0;
        ex_mem_reg.inst <= 0;
        ex_mem_reg.pc <= 0;
        ex_mem_reg.alu_res <= 0;
        ex_mem_reg.read_data_1 <= 0;
        ex_mem_reg.read_data_2 <= 0;
        ex_mem_reg.rd <= 0;
        ex_mem_reg.rs1 <= 0;
        ex_mem_reg.rs2 <= 0;
        ex_mem_reg.we_reg <= 0;
        ex_mem_reg.we_mem <= 0;
        ex_mem_reg.re_mem <= 0;
        ex_mem_reg.wb_sel <= WB_SEL0;
        ex_mem_reg.mem_op <= MEM_NO;
        ex_mem_reg.br_taken <= 0;
        ex_mem_reg.npc_sel <= 0;
        ex_mem_reg.except <= '{default:0};
        ex_mem_reg.csr_val <= 0;
        ex_mem_reg.csr_wdata <= 0;

        mem_wb_reg.valid <= 0;
        mem_wb_reg.inst <= 0;
        mem_wb_reg.pc <= 0;
        mem_wb_reg.alu_res <= 0;
        mem_wb_reg.read_data_1 <= 0;
        mem_wb_reg.read_data_2 <= 0;
        mem_wb_reg.wb_val <= 0;
        mem_wb_reg.rd <= 0;
        mem_wb_reg.rs1 <= 0;
        mem_wb_reg.rs2 <= 0;
        mem_wb_reg.we_reg <= 0;
        mem_wb_reg.we_mem <= 0;
        mem_wb_reg.dmem_wdata <= 0;
        mem_wb_reg.dmem_rdata <= 0;
        mem_wb_reg.br_taken <= 0;
        mem_wb_reg.npc_sel <= 0;
        mem_wb_reg.except <= '{default:0};
        mem_wb_reg.csr_val <= 0;
        mem_wb_reg.csr_wdata <= 0;
      end else if(fsm_stall)begin
      end else if(flush) begin
        if_id_reg.valid <= ~flush;
        if_id_reg.pc <= 0;
        if_id_reg.inst <= 0;
        if_id_reg.except <= '{default:0};
        pc <= next_pc;

        id_ex_reg.valid <= if_id_reg.valid && ~flush;
        id_ex_reg.inst <= 0;
        id_ex_reg.pc <= 0;
        id_ex_reg.read_data_1 <= 0;
        id_ex_reg.read_data_2 <= 0;
        id_ex_reg.imm_value <= 0;
        id_ex_reg.rd <= 0;
        id_ex_reg.rs1 <= 0;
        id_ex_reg.rs2 <= 0;
        id_ex_reg.npc_sel <= 0;
        id_ex_reg.we_reg <= 0;
        id_ex_reg.we_mem <= 0;
        id_ex_reg.re_mem <= 0;
        id_ex_reg.alu_op <= ALU_DEFAULT;
        id_ex_reg.cmp_op <= CMP_NO;
        id_ex_reg.alu_asel <= ASEL0;
        id_ex_reg.alu_bsel <= BSEL0;
        id_ex_reg.wb_sel <= WB_SEL0;
        id_ex_reg.mem_op <= MEM_NO;
        id_ex_reg.except <= '{default:0};
        id_ex_reg.csr_val <= 0;

        ex_mem_reg.valid <= id_ex_reg.valid;
        ex_mem_reg.inst <= id_ex_reg.inst;
        ex_mem_reg.pc <= id_ex_reg.pc;
        ex_mem_reg.alu_res <= alu_res;
        ex_mem_reg.read_data_1 <= id_ex_reg.read_data_1;
        ex_mem_reg.read_data_2 <= id_ex_reg.read_data_2;
        ex_mem_reg.rd <= id_ex_reg.rd;
        ex_mem_reg.rs1 <= id_ex_reg.rs1;
        ex_mem_reg.rs2 <= id_ex_reg.rs2;
        ex_mem_reg.we_reg <= id_ex_reg.we_reg;
        ex_mem_reg.we_mem <= id_ex_reg.we_mem;
        ex_mem_reg.re_mem <= id_ex_reg.re_mem;
        ex_mem_reg.wb_sel <= id_ex_reg.wb_sel;
        ex_mem_reg.mem_op <= id_ex_reg.mem_op;
        ex_mem_reg.br_taken <= br_taken;
        ex_mem_reg.npc_sel <= id_ex_reg.npc_sel;
        ex_mem_reg.except <= except_id_out;
        ex_mem_reg.csr_val <= id_ex_reg.csr_val;
        ex_mem_reg.csr_wdata <= csr_write_res;

        mem_wb_reg.valid <= ex_mem_reg.valid;
        mem_wb_reg.inst <= ex_mem_reg.inst;
        mem_wb_reg.pc <= ex_mem_reg.pc;
        mem_wb_reg.alu_res <= ex_mem_reg.alu_res;
        mem_wb_reg.read_data_1 <= ex_mem_reg.read_data_1;
        mem_wb_reg.read_data_2 <= ex_mem_reg.read_data_2;
        mem_wb_reg.wb_val <= wb_val;
        mem_wb_reg.rd <= ex_mem_reg.rd;
        mem_wb_reg.rs1 <= ex_mem_reg.rs1;
        mem_wb_reg.rs2 <= ex_mem_reg.rs2;
        mem_wb_reg.we_reg <= ex_mem_reg.we_reg;
        mem_wb_reg.we_mem <= ex_mem_reg.we_mem;
        mem_wb_reg.dmem_wdata <= dmem_wdata;
        mem_wb_reg.dmem_rdata <= dmem_rdata;
        mem_wb_reg.br_taken <= ex_mem_reg.br_taken;
        mem_wb_reg.npc_sel <= ex_mem_reg.npc_sel;
        mem_wb_reg.except <= ex_mem_reg.except;
        mem_wb_reg.csr_val <= ex_mem_reg.csr_val;
        mem_wb_reg.csr_wdata <= ex_mem_reg.csr_wdata;
      end else if(load_use_hazard)begin
        if_id_reg.valid <= if_id_reg.valid;
        if_id_reg.pc <= if_id_reg.pc;
        if_id_reg.inst <= if_id_reg.inst;
        if_id_reg.except <= if_id_reg.except;
        pc <= pc;

        id_ex_reg.valid <= 0;
        id_ex_reg.inst <= 0;
        id_ex_reg.pc <= 0;
        id_ex_reg.read_data_1 <= 0;
        id_ex_reg.read_data_2 <= 0;
        id_ex_reg.imm_value <= 0;
        id_ex_reg.rd <= 0;
        id_ex_reg.rs1 <= 0;
        id_ex_reg.rs2 <= 0;
        id_ex_reg.npc_sel <= 0;
        id_ex_reg.we_reg <= 0;
        id_ex_reg.we_mem <= 0;
        id_ex_reg.re_mem <= 0;
        id_ex_reg.alu_op <= ALU_DEFAULT;
        id_ex_reg.cmp_op <= CMP_NO;
        id_ex_reg.alu_asel <= ASEL0;
        id_ex_reg.alu_bsel <= BSEL0;
        id_ex_reg.wb_sel <= WB_SEL0;
        id_ex_reg.mem_op <= MEM_NO;
        id_ex_reg.except <= '{default:0};
        id_ex_reg.csr_val <= 0;

        ex_mem_reg.valid <= id_ex_reg.valid;
        ex_mem_reg.inst <= id_ex_reg.inst;
        ex_mem_reg.pc <= id_ex_reg.pc;
        ex_mem_reg.alu_res <= alu_res;
        ex_mem_reg.read_data_1 <= id_ex_reg.read_data_1;
        ex_mem_reg.read_data_2 <= id_ex_reg.read_data_2;
        ex_mem_reg.rd <= id_ex_reg.rd;
        ex_mem_reg.rs1 <= id_ex_reg.rs1;
        ex_mem_reg.rs2 <= id_ex_reg.rs2;
        ex_mem_reg.we_reg <= id_ex_reg.we_reg;
        ex_mem_reg.we_mem <= id_ex_reg.we_mem;
        ex_mem_reg.re_mem <= id_ex_reg.re_mem;
        ex_mem_reg.wb_sel <= id_ex_reg.wb_sel;
        ex_mem_reg.mem_op <= id_ex_reg.mem_op;
        ex_mem_reg.br_taken <= br_taken;
        ex_mem_reg.npc_sel <= id_ex_reg.npc_sel;
        ex_mem_reg.except <= except_id_out;
        ex_mem_reg.csr_val <= id_ex_reg.csr_val;
        ex_mem_reg.csr_wdata <= csr_write_res;

        mem_wb_reg.valid <= ex_mem_reg.valid;
        mem_wb_reg.inst <= ex_mem_reg.inst;
        mem_wb_reg.pc <= ex_mem_reg.pc;
        mem_wb_reg.alu_res <= ex_mem_reg.alu_res;
        mem_wb_reg.read_data_1 <= ex_mem_reg.read_data_1;
        mem_wb_reg.read_data_2 <= ex_mem_reg.read_data_2;
        mem_wb_reg.wb_val <= wb_val;
        mem_wb_reg.rd <= ex_mem_reg.rd;
        mem_wb_reg.rs1 <= ex_mem_reg.rs1;
        mem_wb_reg.rs2 <= ex_mem_reg.rs2;
        mem_wb_reg.we_reg <= ex_mem_reg.we_reg;
        mem_wb_reg.we_mem <= ex_mem_reg.we_mem;
        mem_wb_reg.dmem_wdata <= dmem_wdata;
        mem_wb_reg.dmem_rdata <= dmem_rdata;
        mem_wb_reg.br_taken <= ex_mem_reg.br_taken;
        mem_wb_reg.npc_sel <= ex_mem_reg.npc_sel;
        mem_wb_reg.except <= ex_mem_reg.except;
        mem_wb_reg.csr_val <= ex_mem_reg.csr_val;
        mem_wb_reg.csr_wdata <= ex_mem_reg.csr_wdata;
      end else begin
        if_id_reg.valid <= ~flush;
        if_id_reg.pc <= pc;
        if_id_reg.inst <= inst;
        if_id_reg.except <= '{default:0};
        pc <= next_pc;

        id_ex_reg.valid <= if_id_reg.valid && ~flush;
        id_ex_reg.inst <= if_id_reg.inst;
        id_ex_reg.pc <= if_id_reg.pc;
        id_ex_reg.read_data_1 <= read_data_1;
        id_ex_reg.read_data_2 <= read_data_2;
        id_ex_reg.imm_value <= imm_value;
        id_ex_reg.rd <= rd;
        id_ex_reg.rs1 <= rs1;
        id_ex_reg.rs2 <= rs2;
        id_ex_reg.npc_sel <= npc_sel;
        id_ex_reg.we_reg <= we_reg;
        id_ex_reg.we_mem <= we_mem;
        id_ex_reg.re_mem <= re_mem;
        id_ex_reg.alu_op <= alu_op;
        id_ex_reg.cmp_op <= cmp_op;
        id_ex_reg.alu_asel <= alu_asel;
        id_ex_reg.alu_bsel <= alu_bsel;
        id_ex_reg.wb_sel <= wb_sel;
        id_ex_reg.mem_op <= mem_op;
        id_ex_reg.except <= if_id_reg.except;
        id_ex_reg.csr_val <= csr_val_id;

        ex_mem_reg.valid <= id_ex_reg.valid;
        ex_mem_reg.inst <= id_ex_reg.inst;
        ex_mem_reg.pc <= id_ex_reg.pc;
        ex_mem_reg.alu_res <= alu_res;
        ex_mem_reg.read_data_1 <= id_ex_reg.read_data_1;
        ex_mem_reg.read_data_2 <= id_ex_reg.read_data_2;
        ex_mem_reg.rd <= id_ex_reg.rd;
        ex_mem_reg.rs1 <= id_ex_reg.rs1;
        ex_mem_reg.rs2 <= id_ex_reg.rs2;
        ex_mem_reg.we_reg <= id_ex_reg.we_reg;
        ex_mem_reg.we_mem <= id_ex_reg.we_mem;
        ex_mem_reg.re_mem <= id_ex_reg.re_mem;
        ex_mem_reg.wb_sel <= id_ex_reg.wb_sel;
        ex_mem_reg.mem_op <= id_ex_reg.mem_op;
        ex_mem_reg.br_taken <= br_taken;
        ex_mem_reg.npc_sel <= id_ex_reg.npc_sel;
        ex_mem_reg.except <= except_id_out;
        ex_mem_reg.csr_val <= id_ex_reg.csr_val;
        ex_mem_reg.csr_wdata <= csr_write_res;

        mem_wb_reg.valid <= ex_mem_reg.valid;
        mem_wb_reg.inst <= ex_mem_reg.inst;
        mem_wb_reg.pc <= ex_mem_reg.pc;
        mem_wb_reg.alu_res <= ex_mem_reg.alu_res;
        mem_wb_reg.read_data_1 <= ex_mem_reg.read_data_1;
        mem_wb_reg.read_data_2 <= ex_mem_reg.read_data_2;
        mem_wb_reg.wb_val <= wb_val;
        mem_wb_reg.rd <= ex_mem_reg.rd;
        mem_wb_reg.rs1 <= ex_mem_reg.rs1;
        mem_wb_reg.rs2 <= ex_mem_reg.rs2;
        mem_wb_reg.we_reg <= ex_mem_reg.we_reg;
        mem_wb_reg.we_mem <= ex_mem_reg.we_mem;
        mem_wb_reg.dmem_wdata <= dmem_wdata;
        mem_wb_reg.dmem_rdata <= dmem_rdata;
        mem_wb_reg.br_taken <= ex_mem_reg.br_taken;
        mem_wb_reg.npc_sel <= ex_mem_reg.npc_sel;
        mem_wb_reg.except <= ex_mem_reg.except;
        mem_wb_reg.csr_val <= ex_mem_reg.csr_val;
        mem_wb_reg.csr_wdata <= ex_mem_reg.csr_wdata;
      end
      end
    end



    assign imem_ift.r_request_bits.raddr = pc;
    assign next_pc = switch_mode ? pc_csr:((id_ex_reg.npc_sel||br_taken) && id_ex_reg.valid) ? alu_res :pc + 4;
    assign flush = (id_ex_reg.npc_sel||br_taken) && id_ex_reg.valid;
    assign dmem_ift.w_request_bits.waddr = ex_mem_reg.alu_res;
    assign dmem_ift.w_request_bits.wdata = dmem_wdata;
    assign dmem_ift.w_request_bits.wmask = dmem_wmask;
    assign dmem_ift.r_request_bits.raddr = ex_mem_reg.alu_res;

    always_comb begin
        case (ex_mem_reg.wb_sel)
            WB_SEL_MEM: wb_val = temp;
            WB_SEL_PC:  wb_val = ex_mem_reg.pc+4 ;
            WB_SEL_CSR: wb_val = ex_mem_reg.csr_val;
            default:    wb_val = ex_mem_reg.alu_res;
        endcase
    end

    CSRModule csr_module (
        .clk(clk),
        .rst(rst),
        .csr_we_wb(mem_wb_reg.valid && !fsm_stall && (mem_wb_reg.inst[6:0] == SYSTEM_OPCODE) && (mem_wb_reg.inst[14:12] != 3'b000) && ((mem_wb_reg.inst[14:12] == 3'b001) || (mem_wb_reg.inst[14:12] == 3'b101) || (mem_wb_reg.inst[19:15] != 5'b0)) && !mem_wb_reg.except.except), 
        .csr_addr_wb(mem_wb_reg.inst[31:20]),
        .csr_val_wb(mem_wb_reg.csr_wdata), 
        .csr_addr_id(if_id_reg.inst[31:20]),
        .csr_val_id(csr_val_id),
        .pc_ret(cosim_interrupt?mem_wb_reg.pc:(mem_wb_reg.npc_sel||mem_wb_reg.br_taken) ? mem_wb_reg.alu_res : mem_wb_reg.pc + 4), 
        .valid_wb(mem_wb_reg.valid && !fsm_stall),
        .time_int(time_int&&!fsm_stall),
        .except_commit((fsm_stall)?'{default:0}:mem_wb_reg.except),
        .csr_ret((mem_wb_reg.inst[6:0]==SYSTEM_OPCODE && mem_wb_reg.inst[14:12]==0 && !fsm_stall) ? 
                 (mem_wb_reg.inst[29] ? 2'b10 : 2'b01) : 2'b00),
        .priv(priv),
        .switch_mode(switch_mode),
        .pc_csr(pc_csr),
        .cosim_interrupt(cosim_interrupt),
        .cosim_cause(cosim_cause),
        .cosim_csr_info(cosim_csr_info)
    );
    assign cosim_switch_mode = switch_mode;
    
    // fill your code

    assign cosim_valid = mem_wb_reg.valid && !fsm_stall && !cosim_interrupt;
    assign cosim_core_info.pc        = mem_wb_reg.pc;
    assign cosim_core_info.inst      = {32'b0,mem_wb_reg.inst};   
    assign cosim_core_info.rs1_id    = {59'b0, mem_wb_reg.rs1};
    assign cosim_core_info.rs1_data  = mem_wb_reg.read_data_1;
    assign cosim_core_info.rs2_id    = {59'b0, mem_wb_reg.rs2};
    assign cosim_core_info.rs2_data  = mem_wb_reg.read_data_2;
    assign cosim_core_info.alu       = mem_wb_reg.alu_res;
    assign cosim_core_info.mem_addr  = mem_wb_reg.alu_res;
    assign cosim_core_info.mem_we    = {63'b0, ex_mem_reg.we_mem && ex_mem_reg.valid && !ex_mem_reg.except.except};
    assign cosim_core_info.mem_wdata = mem_wb_reg.dmem_wdata;
    assign cosim_core_info.mem_rdata = mem_wb_reg.dmem_rdata;
    assign cosim_core_info.rd_we     = {63'b0, mem_wb_reg.we_reg && mem_wb_reg.valid && !fsm_stall && !cosim_interrupt && !mem_wb_reg.except.except};
    assign cosim_core_info.rd_id     = {59'b0, mem_wb_reg.rd}; 
    assign cosim_core_info.rd_data   = mem_wb_reg.wb_val;
    assign cosim_core_info.br_taken  = {63'b0, mem_wb_reg.br_taken};
    assign cosim_core_info.npc       = (mem_wb_reg.npc_sel||mem_wb_reg.br_taken) ? mem_wb_reg.alu_res : mem_wb_reg.pc + 4;

endmodule

