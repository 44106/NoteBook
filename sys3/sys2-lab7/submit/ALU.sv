`include "core_struct.vh"
module ALU (
  input  CorePack::data_t a,
  input  CorePack::data_t b,
  input  CorePack::alu_op_enum  alu_op,
  output CorePack::data_t res
);

  import CorePack::*;

    logic [31:0] a32, b32;       
    logic [31:0] res32_extended; 

always_comb begin
    a32 = 32'h0;
    b32 = 32'h0;
    res32_extended = 32'h0;
  case(alu_op)
    ALU_ADD:res=a+b;
    ALU_SUB:res=a-b;
    ALU_AND:res=a&b;
    ALU_OR:res=a|b;
    ALU_XOR:res=a^b;
    ALU_SLT:res=($signed(a)<$signed(b))?64'd1:64'd0;
    ALU_SLTU:res=(a<b)?64'd1:64'd0;
    ALU_SLL:res=a<<(b[5:0]);
    ALU_SRL:res=a>>(b[5:0]);
    ALU_SRA:res=$signed(a)>>>(b[5:0]);
    ALU_ADDW:begin
                a32=a[31:0];                  
                b32=b[31:0];
                res32_extended=$signed(a32+b32); 
                res={{32{res32_extended[31]}},res32_extended};
            end
    ALU_SUBW:begin
                a32=a[31:0];
                b32=b[31:0];
                res32_extended=$signed($signed(a32)-$signed(b32));
                res={{32{res32_extended[31]}},res32_extended};
            end
    ALU_SLLW:begin
                a32=a[31:0];
                res32_extended=$signed(a32<<b[4:0]);
                res={{32{res32_extended[31]}},res32_extended};
            end
    ALU_SRLW:begin
                a32=a[31:0];
                res32_extended=$signed(a32>>b[4:0]);
                res={{32{res32_extended[31]}},res32_extended};
            end
    ALU_SRAW:begin
                a32=a[31:0];
                res32_extended=$signed($signed(a32)>>>b[4:0]); 
                res={{32{res32_extended[31]}},res32_extended};
            end
    ALU_DEFAULT:res=64'b0;
  endcase
end
  // fill your code

endmodule
