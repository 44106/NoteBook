#include <private_kdefs.h>

    .section .text.init
    .globl _start
_start:
    lla sp, _sbss
    call setup_vm
    call relocate
    call mm_init
    call setup_vm_final
    call clock_set_next_event
    li t0, 0x20
    csrs sie, t0
    li t0, 0x2
    csrs sstatus, t0
    j start_kernel

relocate:
    li t0, PA2VA_OFFSET
    add ra, ra, t0
    add sp, sp, t0
    lla t1, 1f
    add t1, t1, t0
    csrw stvec, t1
    sfence.vma zero, zero
    lla t0, early_pgtbl
    srli t0, t0, 12
    li t1, 8
    slli t1, t1, 60
    or t0, t0, t1
    csrw satp, t0

1:
    sfence.vma zero, zero
    lla t0, _traps
    csrw stvec, t0
    ret

    .section .bss.stack
    .space PGSIZE
