`include "core_struct.vh"
module Controller (
    input CorePack::inst_t inst,
    output we_reg,
    output we_mem,
    output re_mem,
    output npc_sel,
    output CorePack::imm_op_enum immgen_op,
    output CorePack::alu_op_enum alu_op,
    output CorePack::cmp_op_enum cmp_op,
    output CorePack::alu_asel_op_enum alu_asel,
    output CorePack::alu_bsel_op_enum alu_bsel,
    output CorePack::wb_sel_op_enum wb_sel,
    output CorePack::mem_op_enum mem_op
    // output ControllerPack::ControllerSignals ctrl_signals
);

    import CorePack::*;
    // import ControllerPack::*;

wire [6:0] opcode=inst[6:0];
wire [2:0] funct3=inst[14:12];
wire [6:0] funct7=inst[31:25];
wire is_rtype=(opcode==REG_OPCODE);
wire is_itype=(opcode==IMM_OPCODE);
wire is_stype=(opcode==STORE_OPCODE);
wire is_btype=(opcode==BRANCH_OPCODE);
wire is_lui=(opcode==LUI_OPCODE);
wire is_auipc=(opcode==AUIPC_OPCODE);
wire is_jal=(opcode==JAL_OPCODE);
wire is_jalr=(opcode==JALR_OPCODE);
wire is_load=(opcode==LOAD_OPCODE);
wire is_immw=(opcode==IMMW_OPCODE);
wire is_regw=(opcode==REGW_OPCODE);
wire is_system=(opcode==SYSTEM_OPCODE);

always_comb begin
    if (is_rtype||is_itype||is_immw||is_regw)begin
        case(funct3)
            ADD_FUNCT3:begin
                if ((is_rtype||is_regw)&&funct7[5]) 
                    alu_op=(is_regw)?ALU_SUBW:ALU_SUB;
                else 
                    alu_op=(is_regw||is_immw)?ALU_ADDW:ALU_ADD;
            end
            SLL_FUNCT3:alu_op=(is_regw||is_immw)?ALU_SLLW:ALU_SLL;
            SLT_FUNCT3:alu_op=ALU_SLT;
            SLTU_FUNCT3:alu_op=ALU_SLTU;
            XOR_FUNCT3:alu_op=ALU_XOR;
            SRL_FUNCT3:alu_op=(funct7[5])?((is_regw||is_immw)?ALU_SRAW:ALU_SRA):((is_regw||is_immw) ? ALU_SRLW : ALU_SRL);
            OR_FUNCT3:alu_op=ALU_OR;
            AND_FUNCT3:alu_op=ALU_AND;
            default:alu_op=ALU_DEFAULT;
        endcase
    end
    else if(is_auipc||is_jal||is_jalr||is_load||is_btype||is_stype||is_lui)begin
        alu_op=ALU_ADD;
    end
    else begin
        alu_op=ALU_DEFAULT;
    end
end

always_comb begin
    case(opcode)
        LOAD_OPCODE, IMM_OPCODE, JALR_OPCODE,IMMW_OPCODE,SYSTEM_OPCODE: immgen_op=I_IMM;
        STORE_OPCODE:immgen_op=S_IMM;
        BRANCH_OPCODE:immgen_op=B_IMM;
        LUI_OPCODE, AUIPC_OPCODE:immgen_op=U_IMM;
        JAL_OPCODE:immgen_op=UJ_IMM;
        default:immgen_op = IMM0;
    endcase
end

always_comb begin
    if(is_btype)begin
        case(funct3)
            BEQ_FUNCT3:cmp_op=CMP_EQ;
            BNE_FUNCT3:cmp_op=CMP_NE;
            BLT_FUNCT3:cmp_op=CMP_LT;
            BGE_FUNCT3:cmp_op=CMP_GE;
            BLTU_FUNCT3:cmp_op=CMP_LTU;
            BGEU_FUNCT3:cmp_op=CMP_GEU;
            default:cmp_op=CMP_NO;
        endcase
    end
    else begin
        cmp_op=CMP_NO;
    end
end

assign alu_asel=(is_auipc||is_jal||is_btype)?ASEL_PC:(is_lui)?ASEL0:ASEL_REG;
assign alu_bsel=(is_rtype||is_regw)?BSEL_REG:BSEL_IMM;
assign wb_sel=(is_load)?WB_SEL_MEM:(is_jal||is_jalr)?WB_SEL_PC:(is_system&&funct3!=3'b000)?WB_SEL_CSR:WB_SEL0;

always_comb begin
    if (is_load)begin
        case(funct3)
            LB_FUNCT3:mem_op=MEM_B; 
            LH_FUNCT3:mem_op=MEM_H; 
            LW_FUNCT3:mem_op=MEM_W; 
            LD_FUNCT3:mem_op=MEM_D;                     
            LBU_FUNCT3:mem_op=MEM_UB;               
            LHU_FUNCT3:mem_op=MEM_UH;                     
            LWU_FUNCT3:mem_op=MEM_UW;                                  
            default:mem_op=MEM_NO;
        endcase
    end
    else if(is_stype)begin
         case(funct3)
            SB_FUNCT3:mem_op=MEM_B; 
            SH_FUNCT3:mem_op=MEM_H; 
            SW_FUNCT3:mem_op=MEM_W; 
            SD_FUNCT3:mem_op=MEM_D;                                                       
            default:mem_op=MEM_NO;
        endcase
    end
    else begin
        mem_op=MEM_NO;
    end
end


assign we_reg=is_rtype||is_itype||is_lui||is_auipc||is_jal||is_jalr||is_load||is_immw||is_regw||(is_system&&(funct3 != 3'b000));
assign we_mem=is_stype;
assign re_mem=is_load;
assign npc_sel=is_jal||is_jalr;

    
    // fill your code

endmodule
