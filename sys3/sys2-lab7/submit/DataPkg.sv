`include "core_struct.vh"

module DataPkg(
    input CorePack::mem_op_enum mem_op,
    input CorePack::data_t reg_data,
    input CorePack::addr_t dmem_waddr,
    output CorePack::data_t dmem_wdata
);

  import CorePack::*;
 
always_comb begin
   case(mem_op)
      MEM_B:dmem_wdata={56'b0,reg_data[7:0]}<<(dmem_waddr[2:0]*8);
      MEM_H:dmem_wdata={48'b0,reg_data[15:0]}<<(dmem_waddr[2:0]*8);
      MEM_W:dmem_wdata={32'b0,reg_data[31:0]}<<(dmem_waddr[2:0]*8);
      MEM_D:dmem_wdata=reg_data;
      default:dmem_wdata=64'b0;
   endcase
end

  // Data package
  // fill your code

endmodule
