`include "core_struct.vh"

module MaskGen(
    input CorePack::mem_op_enum mem_op,
    input CorePack::addr_t dmem_waddr,
    output CorePack::mask_t dmem_wmask
);

  import CorePack::*;

always_comb begin
   case(mem_op)
      MEM_B:dmem_wmask=8'b0000_0001<<dmem_waddr[2:0];
      MEM_H:dmem_wmask=8'b0000_0011<<dmem_waddr[2:0];
      MEM_W:dmem_wmask=8'b0000_1111<<dmem_waddr[2:0];
      MEM_D:dmem_wmask=8'b1111_1111<<dmem_waddr[2:0];
      default:dmem_wmask=8'b0000_0000<<dmem_waddr[2:0];
   endcase
end

  // Mask generation
  // fill your code

endmodule
