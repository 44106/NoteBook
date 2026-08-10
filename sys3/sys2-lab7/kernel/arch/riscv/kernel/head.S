#include <private_kdefs.h>    
    .section .text.init
    .globl _start
_start:
    # 0. 设置 sp 为 _ekernel 之后 4 KiB 的位置
    la t0, _traps
    csrw stvec, t0
    li t0, 0x20
    csrs sie, t0
#    rdtime t0
#    li t1, TIMECLOCK
#    add a0, t0, t1
#    mv a6, x0
#    mv a7, x0
    li a7, 0x54494d45
    mv a6, x0
    li a0, TIMECLOCK
    ecall
    li t0, 0x2
    csrs sstatus, t0
    la sp, _sbss
    call mm_init

    # 1. 跳转到 start_kernel
    j start_kernel

    .section .bss.stack
    .space PGSIZE
