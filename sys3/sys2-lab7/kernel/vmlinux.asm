
vmlinux:     file format elf64-littleriscv


Disassembly of section .text:

0000000080200000 <_skernel>:
#include <private_kdefs.h>    
    .section .text.init
    .globl _start
_start:
    # 0. 设置 sp 为 _ekernel 之后 4 KiB 的位置
    la t0, _traps
    80200000:	00003297          	auipc	t0,0x3
    80200004:	0282b283          	ld	t0,40(t0) # 80203028 <_GLOBAL_OFFSET_TABLE_+0x28>
    csrw stvec, t0
    80200008:	10529073          	csrw	stvec,t0
    li t0, 0x20
    8020000c:	02000293          	li	t0,32
    csrs sie, t0
    80200010:	1042a073          	csrs	sie,t0
#    rdtime t0
#    li t1, TIMECLOCK
#    add a0, t0, t1
#    mv a6, x0
#    mv a7, x0
    li a7, 0x54494d45
    80200014:	544958b7          	lui	a7,0x54495
    80200018:	d458889b          	addiw	a7,a7,-699 # 54494d45 <_skernel-0x2bd6b2bb>
    mv a6, x0
    8020001c:	00000813          	li	a6,0
    li a0, TIMECLOCK
    80200020:	00031537          	lui	a0,0x31
    80200024:	d405051b          	addiw	a0,a0,-704 # 30d40 <_skernel-0x801cf2c0>
    ecall
    80200028:	00000073          	ecall
    li t0, 0x2
    8020002c:	00200293          	li	t0,2
    csrs sstatus, t0
    80200030:	1002a073          	csrs	sstatus,t0
    la sp, _sbss
    80200034:	00003117          	auipc	sp,0x3
    80200038:	fe413103          	ld	sp,-28(sp) # 80203018 <_GLOBAL_OFFSET_TABLE_+0x18>
    call mm_init
    8020003c:	26c000ef          	jal	ra,802002a8 <mm_init>

    # 1. 跳转到 start_kernel
    j start_kernel
    80200040:	2200006f          	j	80200260 <start_kernel>
	...

0000000080200050 <_traps>:

    # 3. 恢复寄存器和 sepc
    #    特别注意 sp 寄存器的恢复

    # 4. 返回
    addi sp, sp, -288
    80200050:	ee010113          	addi	sp,sp,-288
    sd x1, 0(sp)
    80200054:	00113023          	sd	ra,0(sp)
    sd x2, 8(sp)
    80200058:	00213423          	sd	sp,8(sp)
    sd x3, 16(sp)
    8020005c:	00313823          	sd	gp,16(sp)
    sd x4, 24(sp)
    80200060:	00413c23          	sd	tp,24(sp)
    sd x5, 32(sp)
    80200064:	02513023          	sd	t0,32(sp)
    sd x6, 40(sp)
    80200068:	02613423          	sd	t1,40(sp)
    sd x7, 48(sp)
    8020006c:	02713823          	sd	t2,48(sp)
    sd x8, 56(sp)
    80200070:	02813c23          	sd	s0,56(sp)
    sd x9, 64(sp)
    80200074:	04913023          	sd	s1,64(sp)
    sd x10, 72(sp)
    80200078:	04a13423          	sd	a0,72(sp)
    sd x11, 80(sp)
    8020007c:	04b13823          	sd	a1,80(sp)
    sd x12, 88(sp)
    80200080:	04c13c23          	sd	a2,88(sp)
    sd x13, 96(sp)
    80200084:	06d13023          	sd	a3,96(sp)
    sd x14, 104(sp)
    80200088:	06e13423          	sd	a4,104(sp)
    sd x15, 112(sp)
    8020008c:	06f13823          	sd	a5,112(sp)
    sd x16, 120(sp)
    80200090:	07013c23          	sd	a6,120(sp)
    sd x17, 128(sp)
    80200094:	09113023          	sd	a7,128(sp)
    sd x18, 136(sp)
    80200098:	09213423          	sd	s2,136(sp)
    sd x19, 144(sp)
    8020009c:	09313823          	sd	s3,144(sp)
    sd x20, 152(sp)
    802000a0:	09413c23          	sd	s4,152(sp)
    sd x21, 160(sp)
    802000a4:	0b513023          	sd	s5,160(sp)
    sd x22, 168(sp)
    802000a8:	0b613423          	sd	s6,168(sp)
    sd x23, 176(sp)
    802000ac:	0b713823          	sd	s7,176(sp)
    sd x24, 184(sp)
    802000b0:	0b813c23          	sd	s8,184(sp)
    sd x25, 192(sp)
    802000b4:	0d913023          	sd	s9,192(sp)
    sd x26, 200(sp)
    802000b8:	0da13423          	sd	s10,200(sp)
    sd x27, 208(sp)
    802000bc:	0db13823          	sd	s11,208(sp)
    sd x28, 216(sp)
    802000c0:	0dc13c23          	sd	t3,216(sp)
    sd x29, 224(sp)
    802000c4:	0fd13023          	sd	t4,224(sp)
    sd x30, 232(sp)
    802000c8:	0fe13423          	sd	t5,232(sp)
    sd x31, 240(sp)
    802000cc:	0ff13823          	sd	t6,240(sp)
    csrr t0, sepc
    802000d0:	141022f3          	csrr	t0,sepc
    sd t0, 248(sp)
    802000d4:	0e513c23          	sd	t0,248(sp)
    mv a1, t0
    802000d8:	00028593          	mv	a1,t0
    csrr t0, sstatus
    802000dc:	100022f3          	csrr	t0,sstatus
    sd t0, 256(sp)
    802000e0:	10513023          	sd	t0,256(sp)
    csrr t0, scause
    802000e4:	142022f3          	csrr	t0,scause
    sd t0, 264(sp)
    802000e8:	10513423          	sd	t0,264(sp)
    mv a0, t0
    802000ec:	00028513          	mv	a0,t0
    csrr t0, stval
    802000f0:	143022f3          	csrr	t0,stval
    sd t0, 272(sp)
    802000f4:	10513823          	sd	t0,272(sp)
    call trap_handler
    802000f8:	590000ef          	jal	ra,80200688 <trap_handler>
    ld t0, 256(sp)
    802000fc:	10013283          	ld	t0,256(sp)
    csrw sstatus, t0
    80200100:	10029073          	csrw	sstatus,t0
    ld t0, 248(sp)
    80200104:	0f813283          	ld	t0,248(sp)
    csrw sepc, t0
    80200108:	14129073          	csrw	sepc,t0
    ld x1, 0(sp)
    8020010c:	00013083          	ld	ra,0(sp)
    ld x2, 8(sp)
    80200110:	00813103          	ld	sp,8(sp)
    ld x3, 16(sp)
    80200114:	01013183          	ld	gp,16(sp)
    ld x4, 24(sp)
    80200118:	01813203          	ld	tp,24(sp)
    ld x5, 32(sp)
    8020011c:	02013283          	ld	t0,32(sp)
    ld x6, 40(sp)
    80200120:	02813303          	ld	t1,40(sp)
    ld x7, 48(sp)
    80200124:	03013383          	ld	t2,48(sp)
    ld x8, 56(sp)
    80200128:	03813403          	ld	s0,56(sp)
    ld x9, 64(sp)
    8020012c:	04013483          	ld	s1,64(sp)
    ld x10, 72(sp)
    80200130:	04813503          	ld	a0,72(sp)
    ld x11, 80(sp)
    80200134:	05013583          	ld	a1,80(sp)
    ld x12, 88(sp)
    80200138:	05813603          	ld	a2,88(sp)
    ld x13, 96(sp)
    8020013c:	06013683          	ld	a3,96(sp)
    ld x14, 104(sp)
    80200140:	06813703          	ld	a4,104(sp)
    ld x15, 112(sp)
    80200144:	07013783          	ld	a5,112(sp)
    ld x16, 120(sp)
    80200148:	07813803          	ld	a6,120(sp)
    ld x17, 128(sp)
    8020014c:	08013883          	ld	a7,128(sp)
    ld x18, 136(sp)
    80200150:	08813903          	ld	s2,136(sp)
    ld x19, 144(sp)
    80200154:	09013983          	ld	s3,144(sp)
    ld x20, 152(sp)
    80200158:	09813a03          	ld	s4,152(sp)
    ld x21, 160(sp)
    8020015c:	0a013a83          	ld	s5,160(sp)
    ld x22, 168(sp)
    80200160:	0a813b03          	ld	s6,168(sp)
    ld x23, 176(sp)
    80200164:	0b013b83          	ld	s7,176(sp)
    ld x24, 184(sp)
    80200168:	0b813c03          	ld	s8,184(sp)
    ld x25, 192(sp)
    8020016c:	0c013c83          	ld	s9,192(sp)
    ld x26, 200(sp)
    80200170:	0c813d03          	ld	s10,200(sp)
    ld x27, 208(sp)
    80200174:	0d013d83          	ld	s11,208(sp)
    ld x28, 216(sp)
    80200178:	0d813e03          	ld	t3,216(sp)
    ld x29, 224(sp)
    8020017c:	0e013e83          	ld	t4,224(sp)
    ld x30, 232(sp)
    80200180:	0e813f03          	ld	t5,232(sp)
    ld x31, 240(sp)
    80200184:	0f013f83          	ld	t6,240(sp)
    addi sp, sp, 288
    80200188:	12010113          	addi	sp,sp,288
    sret
    8020018c:	10200073          	sret

0000000080200190 <__dummy>:

    .globl __dummy
__dummy:
    la t0, dummy_task
    80200190:	00003297          	auipc	t0,0x3
    80200194:	e782b283          	ld	t0,-392(t0) # 80203008 <_GLOBAL_OFFSET_TABLE_+0x8>
    csrw sepc, t0
    80200198:	14129073          	csrw	sepc,t0
    sret
    8020019c:	10200073          	sret

00000000802001a0 <__switch_to>:

    .globl __switch_to
__switch_to:
    sd ra, 32(a0)
    802001a0:	02153023          	sd	ra,32(a0)
    sd sp, 40(a0)
    802001a4:	02253423          	sd	sp,40(a0)
    sd s0, 48(a0)
    802001a8:	02853823          	sd	s0,48(a0)
    sd s1, 56(a0)
    802001ac:	02953c23          	sd	s1,56(a0)
    sd s2, 64(a0)
    802001b0:	05253023          	sd	s2,64(a0)
    sd s3, 72(a0)
    802001b4:	05353423          	sd	s3,72(a0)
    sd s4, 80(a0)
    802001b8:	05453823          	sd	s4,80(a0)
    sd s5, 88(a0)
    802001bc:	05553c23          	sd	s5,88(a0)
    sd s6, 96(a0)
    802001c0:	07653023          	sd	s6,96(a0)
    sd s7, 104(a0)
    802001c4:	07753423          	sd	s7,104(a0)
    sd s8, 112(a0)
    802001c8:	07853823          	sd	s8,112(a0)
    sd s9, 120(a0)
    802001cc:	07953c23          	sd	s9,120(a0)
    sd s10, 128(a0)
    802001d0:	09a53023          	sd	s10,128(a0)
    sd s11, 136(a0)
    802001d4:	09b53423          	sd	s11,136(a0)
    ld ra, 32(a1)
    802001d8:	0205b083          	ld	ra,32(a1)
    ld sp, 40(a1)
    802001dc:	0285b103          	ld	sp,40(a1)
    ld s0, 48(a1)
    802001e0:	0305b403          	ld	s0,48(a1)
    ld s1, 56(a1)
    802001e4:	0385b483          	ld	s1,56(a1)
    ld s2, 64(a1)
    802001e8:	0405b903          	ld	s2,64(a1)
    ld s3, 72(a1)
    802001ec:	0485b983          	ld	s3,72(a1)
    ld s4, 80(a1)
    802001f0:	0505ba03          	ld	s4,80(a1)
    ld s5, 88(a1)
    802001f4:	0585ba83          	ld	s5,88(a1)
    ld s6, 96(a1)
    802001f8:	0605bb03          	ld	s6,96(a1)
    ld s7, 104(a1)
    802001fc:	0685bb83          	ld	s7,104(a1)
    ld s8, 112(a1)
    80200200:	0705bc03          	ld	s8,112(a1)
    ld s9, 120(a1)
    80200204:	0785bc83          	ld	s9,120(a1)
    ld s10, 128(a1)
    80200208:	0805bd03          	ld	s10,128(a1)
    ld s11, 136(a1)
    8020020c:	0885bd83          	ld	s11,136(a1)
    80200210:	00008067          	ret
	...

0000000080200220 <clock_set_next_event>:
#include <stdint.h>
#include <private_kdefs.h>
#include <sbi.h>

void clock_set_next_event(void) {
    80200220:	ff010113          	addi	sp,sp,-16
    80200224:	00113423          	sd	ra,8(sp)
	sbi_ecall(0x54494d45, 0, TIMECLOCK, 0, 0, 0, 0, 0);
    80200228:	00000893          	li	a7,0
    8020022c:	00000813          	li	a6,0
    80200230:	00000793          	li	a5,0
    80200234:	00000713          	li	a4,0
    80200238:	00000693          	li	a3,0
    8020023c:	00031637          	lui	a2,0x31
    80200240:	d4060613          	addi	a2,a2,-704 # 30d40 <_skernel-0x801cf2c0>
    80200244:	00000593          	li	a1,0
    80200248:	54495537          	lui	a0,0x54495
    8020024c:	d4550513          	addi	a0,a0,-699 # 54494d45 <_skernel-0x2bd6b2bb>
    80200250:	3c0000ef          	jal	ra,80200610 <sbi_ecall>
}
    80200254:	00813083          	ld	ra,8(sp)
    80200258:	01010113          	addi	sp,sp,16
    8020025c:	00008067          	ret

0000000080200260 <start_kernel>:
#include <printk.h>
#include <sbi.h>
#include <private_kdefs.h>
extern void task_init(void);
_Noreturn void start_kernel(void) {
    80200260:	ff010113          	addi	sp,sp,-16
    80200264:	00113423          	sd	ra,8(sp)
    task_init();
    80200268:	1c0000ef          	jal	ra,80200428 <task_init>
    // �ȴ���һ��ʱ���ж�
    while (1)
    8020026c:	0000006f          	j	8020026c <start_kernel+0xc>

0000000080200270 <alloc_page>:
static struct kfreelist {
  struct kfreelist *next;
} *kfreelist;

void *alloc_page(void) {
  struct kfreelist *r = kfreelist;
    80200270:	00005797          	auipc	a5,0x5
    80200274:	d9078793          	addi	a5,a5,-624 # 80205000 <kfreelist>
    80200278:	0007b503          	ld	a0,0(a5)
  kfreelist = r->next;
    8020027c:	00053703          	ld	a4,0(a0)
    80200280:	00e7b023          	sd	a4,0(a5)
  return r;
}
    80200284:	00008067          	ret

0000000080200288 <free_pages>:

void free_pages(void *addr) {
  struct kfreelist *r = (void *)PGROUNDDOWN((uintptr_t)addr);
    80200288:	fffff7b7          	lui	a5,0xfffff
    8020028c:	00f57533          	and	a0,a0,a5
//  memset(r, 0xfa, PGSIZE);
  r->next = kfreelist;
    80200290:	00005797          	auipc	a5,0x5
    80200294:	d7078793          	addi	a5,a5,-656 # 80205000 <kfreelist>
    80200298:	0007b703          	ld	a4,0(a5)
    8020029c:	00e53023          	sd	a4,0(a0)
  kfreelist = r;
    802002a0:	00a7b023          	sd	a0,0(a5)
}
    802002a4:	00008067          	ret

00000000802002a8 <mm_init>:

void mm_init(void) {
    802002a8:	ff010113          	addi	sp,sp,-16
    802002ac:	00113423          	sd	ra,8(sp)
    802002b0:	00813023          	sd	s0,0(sp)
  uint8_t *s = (void *)PGROUNDUP((uintptr_t)_ekernel);
    802002b4:	00003517          	auipc	a0,0x3
    802002b8:	d5c53503          	ld	a0,-676(a0) # 80203010 <_GLOBAL_OFFSET_TABLE_+0x10>
    802002bc:	000017b7          	lui	a5,0x1
    802002c0:	fff78793          	addi	a5,a5,-1 # fff <_skernel-0x801ff001>
    802002c4:	00f50533          	add	a0,a0,a5
    802002c8:	fffff7b7          	lui	a5,0xfffff
    802002cc:	00f57533          	and	a0,a0,a5
  const uint8_t *e = (void *)PHY_END;
  for (; s + PGSIZE <= e; s += PGSIZE) {
    802002d0:	00c0006f          	j	802002dc <mm_init+0x34>
    free_pages(s);
    802002d4:	fb5ff0ef          	jal	ra,80200288 <free_pages>
  for (; s + PGSIZE <= e; s += PGSIZE) {
    802002d8:	00040513          	mv	a0,s0
    802002dc:	00001437          	lui	s0,0x1
    802002e0:	00850433          	add	s0,a0,s0
    802002e4:	20100793          	li	a5,513
    802002e8:	01679793          	slli	a5,a5,0x16
    802002ec:	fe87f4e3          	bgeu	a5,s0,802002d4 <mm_init+0x2c>
  }

  printk("...mm_init done!\n");
    802002f0:	00002517          	auipc	a0,0x2
    802002f4:	d1050513          	addi	a0,a0,-752 # 80202000 <_srodata>
    802002f8:	088000ef          	jal	ra,80200380 <printk>
}
    802002fc:	00813083          	ld	ra,8(sp)
    80200300:	00013403          	ld	s0,0(sp)
    80200304:	01010113          	addi	sp,sp,16
    80200308:	00008067          	ret

000000008020030c <printk_sbi_write>:
#include <stdio.h>
#include <printk.h>

static int printk_sbi_write(FILE *restrict fp, const void *restrict buf, size_t len) {
    8020030c:	fe010113          	addi	sp,sp,-32
    80200310:	00113c23          	sd	ra,24(sp)
    80200314:	00813823          	sd	s0,16(sp)
    80200318:	00913423          	sd	s1,8(sp)
    8020031c:	01213023          	sd	s2,0(sp)
    80200320:	00058913          	mv	s2,a1
    80200324:	00060493          	mv	s1,a2
  // 调用 SBI 接口输出 buf 中长度为 len 的内容
  // 返回实际输出的字节数
  // Hint：阅读 SBI v2.0 规范！
  char* p = (char*)buf;
  size_t i;
  for (i = 0; i < len; i++) {
    80200328:	00000413          	li	s0,0
    8020032c:	0340006f          	j	80200360 <printk_sbi_write+0x54>
      sbi_ecall(0x4442434e, 2, (uint64_t)(p[i]), 0, 0, 0, 0, 0);
    80200330:	00890533          	add	a0,s2,s0
    80200334:	00000893          	li	a7,0
    80200338:	00000813          	li	a6,0
    8020033c:	00000793          	li	a5,0
    80200340:	00000713          	li	a4,0
    80200344:	00000693          	li	a3,0
    80200348:	00054603          	lbu	a2,0(a0)
    8020034c:	00200593          	li	a1,2
    80200350:	44424537          	lui	a0,0x44424
    80200354:	34e50513          	addi	a0,a0,846 # 4442434e <_skernel-0x3bddbcb2>
    80200358:	2b8000ef          	jal	ra,80200610 <sbi_ecall>
  for (i = 0; i < len; i++) {
    8020035c:	00140413          	addi	s0,s0,1 # 1001 <_skernel-0x801fefff>
    80200360:	fc9468e3          	bltu	s0,s1,80200330 <printk_sbi_write+0x24>
  }return (int)i;
}
    80200364:	0004051b          	sext.w	a0,s0
    80200368:	01813083          	ld	ra,24(sp)
    8020036c:	01013403          	ld	s0,16(sp)
    80200370:	00813483          	ld	s1,8(sp)
    80200374:	00013903          	ld	s2,0(sp)
    80200378:	02010113          	addi	sp,sp,32
    8020037c:	00008067          	ret

0000000080200380 <printk>:

void printk(const char *fmt, ...) {
    80200380:	fa010113          	addi	sp,sp,-96
    80200384:	00113c23          	sd	ra,24(sp)
    80200388:	02b13423          	sd	a1,40(sp)
    8020038c:	02c13823          	sd	a2,48(sp)
    80200390:	02d13c23          	sd	a3,56(sp)
    80200394:	04e13023          	sd	a4,64(sp)
    80200398:	04f13423          	sd	a5,72(sp)
    8020039c:	05013823          	sd	a6,80(sp)
    802003a0:	05113c23          	sd	a7,88(sp)
  FILE printk_out = {
    802003a4:	00000797          	auipc	a5,0x0
    802003a8:	f6878793          	addi	a5,a5,-152 # 8020030c <printk_sbi_write>
    802003ac:	00f13423          	sd	a5,8(sp)
      .write = printk_sbi_write,
  };

  va_list ap;
  va_start(ap, fmt);
    802003b0:	02810613          	addi	a2,sp,40
    802003b4:	00c13023          	sd	a2,0(sp)
  vfprintf(&printk_out, fmt, ap);
    802003b8:	00050593          	mv	a1,a0
    802003bc:	00810513          	addi	a0,sp,8
    802003c0:	1b4010ef          	jal	ra,80201574 <vfprintf>
  va_end(ap);
}
    802003c4:	01813083          	ld	ra,24(sp)
    802003c8:	06010113          	addi	sp,sp,96
    802003cc:	00008067          	ret

00000000802003d0 <dummy_task>:
// - void dummy_task(void);
// - void task_init(void);
// - void do_timer(void);
// - void schedule(void);
// - void switch_to(struct task_struct* next);
void dummy_task(void) {
    802003d0:	fe010113          	addi	sp,sp,-32
    802003d4:	00113c23          	sd	ra,24(sp)
    802003d8:	00813823          	sd	s0,16(sp)
    802003dc:	00913423          	sd	s1,8(sp)
    uint64_t local = 0;
    uint64_t prev_cnt = 0;
    802003e0:	00000413          	li	s0,0
    uint64_t local = 0;
    802003e4:	00000493          	li	s1,0
    802003e8:	0200006f          	j	80200408 <dummy_task+0x38>
        if (current->counter != prev_cnt) {
            // 针对 priority=1 的特殊处理（Lab文档要求）
            if (current->counter == 1) {
                current->counter = 0;
            }
            prev_cnt = current->counter;
    802003ec:	0187b403          	ld	s0,24(a5)
            printk("[PID = %ld] %ld\n", current->pid, ++local);
    802003f0:	00148493          	addi	s1,s1,1
    802003f4:	00048613          	mv	a2,s1
    802003f8:	0007b583          	ld	a1,0(a5)
    802003fc:	00002517          	auipc	a0,0x2
    80200400:	c1c50513          	addi	a0,a0,-996 # 80202018 <_srodata+0x18>
    80200404:	f7dff0ef          	jal	ra,80200380 <printk>
        if (current->counter != prev_cnt) {
    80200408:	00005797          	auipc	a5,0x5
    8020040c:	c007b783          	ld	a5,-1024(a5) # 80205008 <current>
    80200410:	0187b703          	ld	a4,24(a5)
    80200414:	fe870ae3          	beq	a4,s0,80200408 <dummy_task+0x38>
            if (current->counter == 1) {
    80200418:	00100693          	li	a3,1
    8020041c:	fcd718e3          	bne	a4,a3,802003ec <dummy_task+0x1c>
                current->counter = 0;
    80200420:	0007bc23          	sd	zero,24(a5)
    80200424:	fc9ff06f          	j	802003ec <dummy_task+0x1c>

0000000080200428 <task_init>:
        }
    }
}
void task_init(void) {
    80200428:	fe010113          	addi	sp,sp,-32
    8020042c:	00113c23          	sd	ra,24(sp)
    80200430:	00813823          	sd	s0,16(sp)
    80200434:	00913423          	sd	s1,8(sp)
    srand(2025);
    80200438:	7e900513          	li	a0,2025
    8020043c:	3b8000ef          	jal	ra,802007f4 <srand>
    idle = (struct task_struct*)alloc_page();
    80200440:	e31ff0ef          	jal	ra,80200270 <alloc_page>
    80200444:	00005797          	auipc	a5,0x5
    80200448:	bca7b623          	sd	a0,-1076(a5) # 80205010 <idle>
    idle->state = TASK_RUNNING;
    8020044c:	00053423          	sd	zero,8(a0)
    idle->pid = 0;
    80200450:	00053023          	sd	zero,0(a0)
    idle->priority = 0;
    80200454:	00053823          	sd	zero,16(a0)
    idle->counter = 0;
    80200458:	00053c23          	sd	zero,24(a0)
    current = idle;
    8020045c:	00005797          	auipc	a5,0x5
    80200460:	baa7b623          	sd	a0,-1108(a5) # 80205008 <current>
    task[0] = idle;
    80200464:	00005797          	auipc	a5,0x5
    80200468:	baa7ba23          	sd	a0,-1100(a5) # 80205018 <task>
    for (int i = 1; i < NR_TASKS; i++) {
    8020046c:	00100493          	li	s1,1
    80200470:	05c0006f          	j	802004cc <task_init+0xa4>
        struct task_struct* p = (struct task_struct*)alloc_page();
    80200474:	dfdff0ef          	jal	ra,80200270 <alloc_page>
    80200478:	00050413          	mv	s0,a0
        task[i] = p;
    8020047c:	00349713          	slli	a4,s1,0x3
    80200480:	00005797          	auipc	a5,0x5
    80200484:	b9878793          	addi	a5,a5,-1128 # 80205018 <task>
    80200488:	00e787b3          	add	a5,a5,a4
    8020048c:	00a7b023          	sd	a0,0(a5)
        p->state = TASK_RUNNING;
    80200490:	00053423          	sd	zero,8(a0)
        p->pid = i;
    80200494:	00953023          	sd	s1,0(a0)
        p->priority = (rand() % (PRIORITY_MAX - PRIORITY_MIN + 1)) + PRIORITY_MIN;
    80200498:	374000ef          	jal	ra,8020080c <rand>
    8020049c:	00a00593          	li	a1,10
    802004a0:	2f4000ef          	jal	ra,80200794 <__moddi3>
    802004a4:	0015051b          	addiw	a0,a0,1
    802004a8:	00a43823          	sd	a0,16(s0)
        p->counter = 0;
    802004ac:	00043c23          	sd	zero,24(s0)
        p->thread.ra = (uint64_t)__dummy;
    802004b0:	00003797          	auipc	a5,0x3
    802004b4:	b707b783          	ld	a5,-1168(a5) # 80203020 <_GLOBAL_OFFSET_TABLE_+0x20>
    802004b8:	02f43023          	sd	a5,32(s0)
        p->thread.sp = (uint64_t)p + PGSIZE;
    802004bc:	000017b7          	lui	a5,0x1
    802004c0:	00f407b3          	add	a5,s0,a5
    802004c4:	02f43423          	sd	a5,40(s0)
    for (int i = 1; i < NR_TASKS; i++) {
    802004c8:	0014849b          	addiw	s1,s1,1
    802004cc:	00400793          	li	a5,4
    802004d0:	fa97d2e3          	bge	a5,s1,80200474 <task_init+0x4c>
    }
    printk("...task_init done!\n");
    802004d4:	00002517          	auipc	a0,0x2
    802004d8:	b5c50513          	addi	a0,a0,-1188 # 80202030 <_srodata+0x30>
    802004dc:	ea5ff0ef          	jal	ra,80200380 <printk>
}
    802004e0:	01813083          	ld	ra,24(sp)
    802004e4:	01013403          	ld	s0,16(sp)
    802004e8:	00813483          	ld	s1,8(sp)
    802004ec:	02010113          	addi	sp,sp,32
    802004f0:	00008067          	ret

00000000802004f4 <switch_to>:
void switch_to(struct task_struct* next) {
    802004f4:	00050593          	mv	a1,a0
    if (current == next) {
    802004f8:	00005517          	auipc	a0,0x5
    802004fc:	b1053503          	ld	a0,-1264(a0) # 80205008 <current>
    80200500:	02b50263          	beq	a0,a1,80200524 <switch_to+0x30>
void switch_to(struct task_struct* next) {
    80200504:	ff010113          	addi	sp,sp,-16
    80200508:	00113423          	sd	ra,8(sp)
        return;
    }
    struct task_struct* prev = current;
    current = next;
    8020050c:	00005797          	auipc	a5,0x5
    80200510:	aeb7be23          	sd	a1,-1284(a5) # 80205008 <current>
    __switch_to(prev, next);
    80200514:	c8dff0ef          	jal	ra,802001a0 <__switch_to>
}
    80200518:	00813083          	ld	ra,8(sp)
    8020051c:	01010113          	addi	sp,sp,16
    80200520:	00008067          	ret
    80200524:	00008067          	ret

0000000080200528 <schedule>:
        current->counter = 0; 
        schedule();
    }
}

void schedule(void) {
    80200528:	ff010113          	addi	sp,sp,-16
    8020052c:	00113423          	sd	ra,8(sp)
    80200530:	0740006f          	j	802005a4 <schedule+0x7c>
    struct task_struct* next = NULL;
    long max_c = -1;
    while (1) {
        max_c = -1; 
        next = NULL;
        for (int i = 0; i < NR_TASKS; i++) {
    80200534:	0017879b          	addiw	a5,a5,1
    80200538:	00400713          	li	a4,4
    8020053c:	02f74a63          	blt	a4,a5,80200570 <schedule+0x48>
            if (task[i]->state == TASK_RUNNING) {
    80200540:	00379693          	slli	a3,a5,0x3
    80200544:	00005717          	auipc	a4,0x5
    80200548:	ad470713          	addi	a4,a4,-1324 # 80205018 <task>
    8020054c:	00d70733          	add	a4,a4,a3
    80200550:	00073703          	ld	a4,0(a4)
    80200554:	00873683          	ld	a3,8(a4)
    80200558:	fc069ee3          	bnez	a3,80200534 <schedule+0xc>
                if ((long)task[i]->counter > max_c) {
    8020055c:	01873683          	ld	a3,24(a4)
    80200560:	fcd65ae3          	bge	a2,a3,80200534 <schedule+0xc>
                    max_c = task[i]->counter;
    80200564:	00068613          	mv	a2,a3
                    next = task[i];
    80200568:	00070513          	mv	a0,a4
    8020056c:	fc9ff06f          	j	80200534 <schedule+0xc>
                }
            }
        }
        if (max_c > 0) {
    80200570:	04c04263          	bgtz	a2,802005b4 <schedule+0x8c>
            break;
        }
        for (int i = 0; i < NR_TASKS; i++) {
    80200574:	00000793          	li	a5,0
    80200578:	0240006f          	j	8020059c <schedule+0x74>
            task[i]->counter = task[i]->priority;
    8020057c:	00379693          	slli	a3,a5,0x3
    80200580:	00005717          	auipc	a4,0x5
    80200584:	a9870713          	addi	a4,a4,-1384 # 80205018 <task>
    80200588:	00d70733          	add	a4,a4,a3
    8020058c:	00073703          	ld	a4,0(a4)
    80200590:	01073683          	ld	a3,16(a4)
    80200594:	00d73c23          	sd	a3,24(a4)
        for (int i = 0; i < NR_TASKS; i++) {
    80200598:	0017879b          	addiw	a5,a5,1
    8020059c:	00400713          	li	a4,4
    802005a0:	fcf75ee3          	bge	a4,a5,8020057c <schedule+0x54>
        for (int i = 0; i < NR_TASKS; i++) {
    802005a4:	00000793          	li	a5,0
        max_c = -1; 
    802005a8:	fff00613          	li	a2,-1
        next = NULL;
    802005ac:	00000513          	li	a0,0
        for (int i = 0; i < NR_TASKS; i++) {
    802005b0:	f89ff06f          	j	80200538 <schedule+0x10>
        }
    }
    switch_to(next);
    802005b4:	f41ff0ef          	jal	ra,802004f4 <switch_to>
}
    802005b8:	00813083          	ld	ra,8(sp)
    802005bc:	01010113          	addi	sp,sp,16
    802005c0:	00008067          	ret

00000000802005c4 <do_timer>:
void do_timer(void) {
    802005c4:	ff010113          	addi	sp,sp,-16
    802005c8:	00113423          	sd	ra,8(sp)
    if (current == idle || current->counter == 0) {
    802005cc:	00005717          	auipc	a4,0x5
    802005d0:	a3c73703          	ld	a4,-1476(a4) # 80205008 <current>
    802005d4:	00005797          	auipc	a5,0x5
    802005d8:	a3c7b783          	ld	a5,-1476(a5) # 80205010 <idle>
    802005dc:	02f70263          	beq	a4,a5,80200600 <do_timer+0x3c>
    802005e0:	01873783          	ld	a5,24(a4)
    802005e4:	00078e63          	beqz	a5,80200600 <do_timer+0x3c>
    current->counter--;
    802005e8:	fff78793          	addi	a5,a5,-1
    802005ec:	00f73c23          	sd	a5,24(a4)
    if (current->counter > 0) {
    802005f0:	00079a63          	bnez	a5,80200604 <do_timer+0x40>
        current->counter = 0; 
    802005f4:	00073c23          	sd	zero,24(a4)
        schedule();
    802005f8:	f31ff0ef          	jal	ra,80200528 <schedule>
    802005fc:	0080006f          	j	80200604 <do_timer+0x40>
        schedule();
    80200600:	f29ff0ef          	jal	ra,80200528 <schedule>
}
    80200604:	00813083          	ld	ra,8(sp)
    80200608:	01010113          	addi	sp,sp,16
    8020060c:	00008067          	ret

0000000080200610 <sbi_ecall>:
#include <stdint.h>
#include <sbi.h>

struct sbiret sbi_ecall(uint64_t eid, uint64_t fid,
                        uint64_t arg0, uint64_t arg1, uint64_t arg2,
                        uint64_t arg3, uint64_t arg4, uint64_t arg5) {
    80200610:	fd010113          	addi	sp,sp,-48
    80200614:	02813423          	sd	s0,40(sp)
    80200618:	00050413          	mv	s0,a0
    8020061c:	00058393          	mv	t2,a1
    80200620:	00060e13          	mv	t3,a2
    80200624:	00068313          	mv	t1,a3
    80200628:	00070e93          	mv	t4,a4
    8020062c:	00078f13          	mv	t5,a5
    80200630:	00080f93          	mv	t6,a6
    80200634:	00088293          	mv	t0,a7
    struct sbiret ret;
    asm volatile(
    80200638:	000e0513          	mv	a0,t3
    8020063c:	00030593          	mv	a1,t1
    80200640:	000e8613          	mv	a2,t4
    80200644:	000f0693          	mv	a3,t5
    80200648:	000f8713          	mv	a4,t6
    8020064c:	00028793          	mv	a5,t0
    80200650:	00038813          	mv	a6,t2
    80200654:	00040893          	mv	a7,s0
    80200658:	00000073          	ecall
    8020065c:	00050e13          	mv	t3,a0
    80200660:	00058313          	mv	t1,a1
    80200664:	01c13023          	sd	t3,0(sp)
    80200668:	00613423          	sd	t1,8(sp)
        "mv %[value], a1\n"
        : [error] "=r"(ret.error), [value] "=r"(ret.value)
        : [arg0] "r"(arg0), [arg1] "r"(arg1), [arg2] "r"(arg2), [arg3] "r"(arg3), [arg4] "r"(arg4), [arg5] "r"(arg5), [fid] "r"(fid), [eid] "r"(eid)
        : "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "memory"
        );
    return ret;
    8020066c:	01c13823          	sd	t3,16(sp)
    80200670:	00613c23          	sd	t1,24(sp)
}
    80200674:	000e0513          	mv	a0,t3
    80200678:	00030593          	mv	a1,t1
    8020067c:	02813403          	ld	s0,40(sp)
    80200680:	03010113          	addi	sp,sp,48
    80200684:	00008067          	ret

0000000080200688 <trap_handler>:
#include <stdint.h>
#include <printk.h>

void clock_set_next_event(void);
extern void do_timer(void);
void trap_handler(uint64_t scause, uint64_t sepc) {
    80200688:	ff010113          	addi	sp,sp,-16
    8020068c:	00113423          	sd	ra,8(sp)
  // 根据 scause 判断 trap 类型
  // 如果是 Supervisor Timer Interrupt：
  // - 打印输出相关信息
  // - 调用 clock_set_next_event 设置下一次时钟中断
  // 其他类型的 trap 可以直接忽略，推荐打印出来供以后调试
	if (scause == 0x8000000000000005) {
    80200690:	fff00793          	li	a5,-1
    80200694:	03f79793          	slli	a5,a5,0x3f
    80200698:	00578793          	addi	a5,a5,5
    8020069c:	02f50463          	beq	a0,a5,802006c4 <trap_handler+0x3c>
    802006a0:	00058613          	mv	a2,a1
		clock_set_next_event();
		do_timer();
	}
	else {
		printk("Unhandled trap: scause=%lx, sepc=%lx\n", scause, sepc);
    802006a4:	00050593          	mv	a1,a0
    802006a8:	00002517          	auipc	a0,0x2
    802006ac:	9a050513          	addi	a0,a0,-1632 # 80202048 <_srodata+0x48>
    802006b0:	cd1ff0ef          	jal	ra,80200380 <printk>
		clock_set_next_event();
    802006b4:	b6dff0ef          	jal	ra,80200220 <clock_set_next_event>
	}
}
    802006b8:	00813083          	ld	ra,8(sp)
    802006bc:	01010113          	addi	sp,sp,16
    802006c0:	00008067          	ret
		clock_set_next_event();
    802006c4:	b5dff0ef          	jal	ra,80200220 <clock_set_next_event>
		do_timer();
    802006c8:	efdff0ef          	jal	ra,802005c4 <do_timer>
    802006cc:	fedff06f          	j	802006b8 <trap_handler+0x30>

00000000802006d0 <__udivsi3>:
# define __divdi3 __divsi3
# define __moddi3 __modsi3
#else
FUNC_BEGIN (__udivsi3)
  /* Compute __udivdi3(a0 << 32, a1 << 32); cast result to uint32_t.  */
  sll    a0, a0, 32
    802006d0:	02051513          	slli	a0,a0,0x20
  sll    a1, a1, 32
    802006d4:	02059593          	slli	a1,a1,0x20
  move   t0, ra
    802006d8:	00008293          	mv	t0,ra
  jal    HIDDEN_JUMPTARGET(__udivdi3)
    802006dc:	03c000ef          	jal	ra,80200718 <__hidden___udivdi3>
  sext.w a0, a0
    802006e0:	0005051b          	sext.w	a0,a0
  jr     t0
    802006e4:	00028067          	jr	t0

00000000802006e8 <__umodsi3>:
FUNC_END (__udivsi3)

FUNC_BEGIN (__umodsi3)
  /* Compute __udivdi3((uint32_t)a0, (uint32_t)a1); cast a1 to uint32_t.  */
  sll    a0, a0, 32
    802006e8:	02051513          	slli	a0,a0,0x20
  sll    a1, a1, 32
    802006ec:	02059593          	slli	a1,a1,0x20
  srl    a0, a0, 32
    802006f0:	02055513          	srli	a0,a0,0x20
  srl    a1, a1, 32
    802006f4:	0205d593          	srli	a1,a1,0x20
  move   t0, ra
    802006f8:	00008293          	mv	t0,ra
  jal    HIDDEN_JUMPTARGET(__udivdi3)
    802006fc:	01c000ef          	jal	ra,80200718 <__hidden___udivdi3>
  sext.w a0, a1
    80200700:	0005851b          	sext.w	a0,a1
  jr     t0
    80200704:	00028067          	jr	t0

0000000080200708 <__divsi3>:

FUNC_ALIAS (__modsi3, __moddi3)

FUNC_BEGIN( __divsi3)
  /* Check for special case of INT_MIN/-1. Otherwise, fall into __divdi3.  */
  li    t0, -1
    80200708:	fff00293          	li	t0,-1
  beq   a1, t0, .L20
    8020070c:	0a558c63          	beq	a1,t0,802007c4 <__moddi3+0x30>

0000000080200710 <__divdi3>:
#endif

FUNC_BEGIN (__divdi3)
  bltz  a0, .L10
    80200710:	06054063          	bltz	a0,80200770 <__umoddi3+0x10>
  bltz  a1, .L11
    80200714:	0605c663          	bltz	a1,80200780 <__umoddi3+0x20>

0000000080200718 <__hidden___udivdi3>:
  /* Since the quotient is positive, fall into __udivdi3.  */

FUNC_BEGIN (__udivdi3)
  mv    a2, a1
    80200718:	00058613          	mv	a2,a1
  mv    a1, a0
    8020071c:	00050593          	mv	a1,a0
  li    a0, -1
    80200720:	fff00513          	li	a0,-1
  beqz  a2, .L5
    80200724:	02060c63          	beqz	a2,8020075c <__hidden___udivdi3+0x44>
  li    a3, 1
    80200728:	00100693          	li	a3,1
  bgeu  a2, a1, .L2
    8020072c:	00b67a63          	bgeu	a2,a1,80200740 <__hidden___udivdi3+0x28>
.L1:
  blez  a2, .L2
    80200730:	00c05863          	blez	a2,80200740 <__hidden___udivdi3+0x28>
  slli  a2, a2, 1
    80200734:	00161613          	slli	a2,a2,0x1
  slli  a3, a3, 1
    80200738:	00169693          	slli	a3,a3,0x1
  bgtu  a1, a2, .L1
    8020073c:	feb66ae3          	bltu	a2,a1,80200730 <__hidden___udivdi3+0x18>
.L2:
  li    a0, 0
    80200740:	00000513          	li	a0,0
.L3:
  bltu  a1, a2, .L4
    80200744:	00c5e663          	bltu	a1,a2,80200750 <__hidden___udivdi3+0x38>
  sub   a1, a1, a2
    80200748:	40c585b3          	sub	a1,a1,a2
  or    a0, a0, a3
    8020074c:	00d56533          	or	a0,a0,a3
.L4:
  srli  a3, a3, 1
    80200750:	0016d693          	srli	a3,a3,0x1
  srli  a2, a2, 1
    80200754:	00165613          	srli	a2,a2,0x1
  bnez  a3, .L3
    80200758:	fe0696e3          	bnez	a3,80200744 <__hidden___udivdi3+0x2c>
.L5:
  ret
    8020075c:	00008067          	ret

0000000080200760 <__umoddi3>:
FUNC_END (__udivdi3)
HIDDEN_DEF (__udivdi3)

FUNC_BEGIN (__umoddi3)
  /* Call __udivdi3(a0, a1), then return the remainder, which is in a1.  */
  move  t0, ra
    80200760:	00008293          	mv	t0,ra
  jal   HIDDEN_JUMPTARGET(__udivdi3)
    80200764:	fb5ff0ef          	jal	ra,80200718 <__hidden___udivdi3>
  move  a0, a1
    80200768:	00058513          	mv	a0,a1
  jr    t0
    8020076c:	00028067          	jr	t0
FUNC_END (__umoddi3)

  /* Handle negative arguments to __divdi3.  */
.L10:
  neg   a0, a0
    80200770:	40a00533          	neg	a0,a0
  /* Zero is handled as a negative so that the result will not be inverted.  */
  bgtz  a1, .L12     /* Compute __udivdi3(-a0, a1), then negate the result.  */
    80200774:	00b04863          	bgtz	a1,80200784 <__umoddi3+0x24>

  neg   a1, a1
    80200778:	40b005b3          	neg	a1,a1
  j     HIDDEN_JUMPTARGET(__udivdi3)     /* Compute __udivdi3(-a0, -a1).  */
    8020077c:	f9dff06f          	j	80200718 <__hidden___udivdi3>
.L11:                /* Compute __udivdi3(a0, -a1), then negate the result.  */
  neg   a1, a1
    80200780:	40b005b3          	neg	a1,a1
.L12:
  move  t0, ra
    80200784:	00008293          	mv	t0,ra
  jal   HIDDEN_JUMPTARGET(__udivdi3)
    80200788:	f91ff0ef          	jal	ra,80200718 <__hidden___udivdi3>
  neg   a0, a0
    8020078c:	40a00533          	neg	a0,a0
  jr    t0
    80200790:	00028067          	jr	t0

0000000080200794 <__moddi3>:
FUNC_END (__divdi3)

FUNC_BEGIN (__moddi3)
  move   t0, ra
    80200794:	00008293          	mv	t0,ra
  bltz   a1, .L31
    80200798:	0005ca63          	bltz	a1,802007ac <__moddi3+0x18>
  bltz   a0, .L32
    8020079c:	00054c63          	bltz	a0,802007b4 <__moddi3+0x20>
.L30:
  jal    HIDDEN_JUMPTARGET(__udivdi3)    /* The dividend is not negative.  */
    802007a0:	f79ff0ef          	jal	ra,80200718 <__hidden___udivdi3>
  move   a0, a1
    802007a4:	00058513          	mv	a0,a1
  jr     t0
    802007a8:	00028067          	jr	t0
.L31:
  neg    a1, a1
    802007ac:	40b005b3          	neg	a1,a1
  bgez   a0, .L30
    802007b0:	fe0558e3          	bgez	a0,802007a0 <__moddi3+0xc>
.L32:
  neg    a0, a0
    802007b4:	40a00533          	neg	a0,a0
  jal    HIDDEN_JUMPTARGET(__udivdi3)    /* The dividend is hella negative.  */
    802007b8:	f61ff0ef          	jal	ra,80200718 <__hidden___udivdi3>
  neg    a0, a1
    802007bc:	40b00533          	neg	a0,a1
  jr     t0
    802007c0:	00028067          	jr	t0
FUNC_END (__moddi3)

#if __riscv_xlen == 64
  /* continuation of __divsi3 */
.L20:
  sll   t0, t0, 31
    802007c4:	01f29293          	slli	t0,t0,0x1f
  bne   a0, t0, __divdi3
    802007c8:	f45514e3          	bne	a0,t0,80200710 <__divdi3>
  ret
    802007cc:	00008067          	ret

00000000802007d0 <__muldi3>:
/* Our RV64 64-bit routine is equivalent to our RV32 32-bit routine.  */
# define __muldi3 __mulsi3
#endif

FUNC_BEGIN (__muldi3)
  mv     a2, a0
    802007d0:	00050613          	mv	a2,a0
  li     a0, 0
    802007d4:	00000513          	li	a0,0
.L1:
  andi   a3, a1, 1
    802007d8:	0015f693          	andi	a3,a1,1
  beqz   a3, .L2
    802007dc:	00068463          	beqz	a3,802007e4 <__muldi3+0x14>
  add    a0, a0, a2
    802007e0:	00c50533          	add	a0,a0,a2
.L2:
  srli   a1, a1, 1
    802007e4:	0015d593          	srli	a1,a1,0x1
  slli   a2, a2, 1
    802007e8:	00161613          	slli	a2,a2,0x1
  bnez   a1, .L1
    802007ec:	fe0596e3          	bnez	a1,802007d8 <__muldi3+0x8>
  ret
    802007f0:	00008067          	ret

00000000802007f4 <srand>:
#include <stdint.h>

static uint64_t seed;

void srand(unsigned s) {
  seed = s - 1;
    802007f4:	fff5051b          	addiw	a0,a0,-1
    802007f8:	02051513          	slli	a0,a0,0x20
    802007fc:	02055513          	srli	a0,a0,0x20
    80200800:	00005797          	auipc	a5,0x5
    80200804:	84a7b023          	sd	a0,-1984(a5) # 80205040 <seed>
}
    80200808:	00008067          	ret

000000008020080c <rand>:

int rand(void) {
  seed = 6364136223846793005ULL * seed + 1;
    8020080c:	00005617          	auipc	a2,0x5
    80200810:	83460613          	addi	a2,a2,-1996 # 80205040 <seed>
    80200814:	00063783          	ld	a5,0(a2)
    80200818:	00479693          	slli	a3,a5,0x4
    8020081c:	40f686b3          	sub	a3,a3,a5
    80200820:	00669713          	slli	a4,a3,0x6
    80200824:	40d70733          	sub	a4,a4,a3
    80200828:	00771693          	slli	a3,a4,0x7
    8020082c:	00d70733          	add	a4,a4,a3
    80200830:	00271693          	slli	a3,a4,0x2
    80200834:	00f68733          	add	a4,a3,a5
    80200838:	00671693          	slli	a3,a4,0x6
    8020083c:	40e68733          	sub	a4,a3,a4
    80200840:	00771693          	slli	a3,a4,0x7
    80200844:	00f686b3          	add	a3,a3,a5
    80200848:	00269713          	slli	a4,a3,0x2
    8020084c:	00f70733          	add	a4,a4,a5
    80200850:	00371693          	slli	a3,a4,0x3
    80200854:	40e686b3          	sub	a3,a3,a4
    80200858:	00369713          	slli	a4,a3,0x3
    8020085c:	40d70733          	sub	a4,a4,a3
    80200860:	00671693          	slli	a3,a4,0x6
    80200864:	40e686b3          	sub	a3,a3,a4
    80200868:	00269713          	slli	a4,a3,0x2
    8020086c:	40f70733          	sub	a4,a4,a5
    80200870:	00771693          	slli	a3,a4,0x7
    80200874:	40f686b3          	sub	a3,a3,a5
    80200878:	00269713          	slli	a4,a3,0x2
    8020087c:	00f70733          	add	a4,a4,a5
    80200880:	00271693          	slli	a3,a4,0x2
    80200884:	40f686b3          	sub	a3,a3,a5
    80200888:	00269713          	slli	a4,a3,0x2
    8020088c:	40f70733          	sub	a4,a4,a5
    80200890:	00271513          	slli	a0,a4,0x2
    80200894:	00f50533          	add	a0,a0,a5
    80200898:	00150513          	addi	a0,a0,1
    8020089c:	00a63023          	sd	a0,0(a2)
  return seed >> 33;
}
    802008a0:	02155513          	srli	a0,a0,0x21
    802008a4:	00008067          	ret

00000000802008a8 <memset>:
#include <string.h>

void *memset(void *restrict dst, int c, size_t n) {
	char* p = (char*)dst;
	for (size_t i = 0; i < n; i++) {
    802008a8:	00000793          	li	a5,0
    802008ac:	0100006f          	j	802008bc <memset+0x14>
		p[i] = (char)c;
    802008b0:	00f50733          	add	a4,a0,a5
    802008b4:	00b70023          	sb	a1,0(a4)
	for (size_t i = 0; i < n; i++) {
    802008b8:	00178793          	addi	a5,a5,1
    802008bc:	fec7eae3          	bltu	a5,a2,802008b0 <memset+0x8>
	}return dst;
}
    802008c0:	00008067          	ret

00000000802008c4 <strnlen>:

size_t strnlen(const char *restrict s, size_t maxlen) {
    802008c4:	00050713          	mv	a4,a0
	size_t i = 0;
    802008c8:	00000513          	li	a0,0
	while (i < maxlen && s[i] != '\0') {
    802008cc:	0080006f          	j	802008d4 <strnlen+0x10>
		i++;
    802008d0:	00150513          	addi	a0,a0,1
	while (i < maxlen && s[i] != '\0') {
    802008d4:	00b57863          	bgeu	a0,a1,802008e4 <strnlen+0x20>
    802008d8:	00a707b3          	add	a5,a4,a0
    802008dc:	0007c783          	lbu	a5,0(a5)
    802008e0:	fe0798e3          	bnez	a5,802008d0 <strnlen+0xc>
	}return i;
}
    802008e4:	00008067          	ret

00000000802008e8 <pop_arg>:
  // long double f;
  void *p;
};

static void pop_arg(union arg *arg, int type, va_list *ap) {
  switch (type) {
    802008e8:	ff85859b          	addiw	a1,a1,-8
    802008ec:	0005871b          	sext.w	a4,a1
    802008f0:	00f00793          	li	a5,15
    802008f4:	1ae7e063          	bltu	a5,a4,80200a94 <pop_arg+0x1ac>
    802008f8:	02059793          	slli	a5,a1,0x20
    802008fc:	01e7d593          	srli	a1,a5,0x1e
    80200900:	00001717          	auipc	a4,0x1
    80200904:	77070713          	addi	a4,a4,1904 # 80202070 <_srodata+0x70>
    80200908:	00e585b3          	add	a1,a1,a4
    8020090c:	0005a783          	lw	a5,0(a1)
    80200910:	00e787b3          	add	a5,a5,a4
    80200914:	00078067          	jr	a5
    case PTR:
      arg->p = va_arg(*ap, void *);
    80200918:	00063783          	ld	a5,0(a2)
    8020091c:	00878713          	addi	a4,a5,8
    80200920:	00e63023          	sd	a4,0(a2)
    80200924:	0007b783          	ld	a5,0(a5)
    80200928:	00f53023          	sd	a5,0(a0)
      break;
    8020092c:	00008067          	ret
    case INT:
      arg->i = va_arg(*ap, int);
    80200930:	00063783          	ld	a5,0(a2)
    80200934:	00878713          	addi	a4,a5,8
    80200938:	00e63023          	sd	a4,0(a2)
    8020093c:	0007a783          	lw	a5,0(a5)
    80200940:	00f53023          	sd	a5,0(a0)
      break;
    80200944:	00008067          	ret
    case UINT:
      arg->i = va_arg(*ap, unsigned int);
    80200948:	00063783          	ld	a5,0(a2)
    8020094c:	00878713          	addi	a4,a5,8
    80200950:	00e63023          	sd	a4,0(a2)
    80200954:	0007e783          	lwu	a5,0(a5)
    80200958:	00f53023          	sd	a5,0(a0)
      break;
    8020095c:	00008067          	ret
    case LONG:
      arg->i = va_arg(*ap, long);
    80200960:	00063783          	ld	a5,0(a2)
    80200964:	00878713          	addi	a4,a5,8
    80200968:	00e63023          	sd	a4,0(a2)
    8020096c:	0007b783          	ld	a5,0(a5)
    80200970:	00f53023          	sd	a5,0(a0)
      break;
    80200974:	00008067          	ret
    case ULONG:
      arg->i = va_arg(*ap, unsigned long);
    80200978:	00063783          	ld	a5,0(a2)
    8020097c:	00878713          	addi	a4,a5,8
    80200980:	00e63023          	sd	a4,0(a2)
    80200984:	0007b783          	ld	a5,0(a5)
    80200988:	00f53023          	sd	a5,0(a0)
      break;
    8020098c:	00008067          	ret
    case ULLONG:
      arg->i = va_arg(*ap, unsigned long long);
    80200990:	00063783          	ld	a5,0(a2)
    80200994:	00878713          	addi	a4,a5,8
    80200998:	00e63023          	sd	a4,0(a2)
    8020099c:	0007b783          	ld	a5,0(a5)
    802009a0:	00f53023          	sd	a5,0(a0)
      break;
    802009a4:	00008067          	ret
    case SHORT:
      arg->i = (short)va_arg(*ap, int);
    802009a8:	00063783          	ld	a5,0(a2)
    802009ac:	00878713          	addi	a4,a5,8
    802009b0:	00e63023          	sd	a4,0(a2)
    802009b4:	00079783          	lh	a5,0(a5)
    802009b8:	00f53023          	sd	a5,0(a0)
      break;
    802009bc:	00008067          	ret
    case USHORT:
      arg->i = (unsigned short)va_arg(*ap, int);
    802009c0:	00063783          	ld	a5,0(a2)
    802009c4:	00878713          	addi	a4,a5,8
    802009c8:	00e63023          	sd	a4,0(a2)
    802009cc:	0007d783          	lhu	a5,0(a5)
    802009d0:	00f53023          	sd	a5,0(a0)
      break;
    802009d4:	00008067          	ret
    case CHAR:
      arg->i = (signed char)va_arg(*ap, int);
    802009d8:	00063783          	ld	a5,0(a2)
    802009dc:	00878713          	addi	a4,a5,8
    802009e0:	00e63023          	sd	a4,0(a2)
    802009e4:	00078783          	lb	a5,0(a5)
    802009e8:	00f53023          	sd	a5,0(a0)
      break;
    802009ec:	00008067          	ret
    case UCHAR:
      arg->i = (unsigned char)va_arg(*ap, int);
    802009f0:	00063783          	ld	a5,0(a2)
    802009f4:	00878713          	addi	a4,a5,8
    802009f8:	00e63023          	sd	a4,0(a2)
    802009fc:	0007c783          	lbu	a5,0(a5)
    80200a00:	00f53023          	sd	a5,0(a0)
      break;
    80200a04:	00008067          	ret
    case LLONG:
      arg->i = va_arg(*ap, long long);
    80200a08:	00063783          	ld	a5,0(a2)
    80200a0c:	00878713          	addi	a4,a5,8
    80200a10:	00e63023          	sd	a4,0(a2)
    80200a14:	0007b783          	ld	a5,0(a5)
    80200a18:	00f53023          	sd	a5,0(a0)
      break;
    80200a1c:	00008067          	ret
    case SIZET:
      arg->i = va_arg(*ap, size_t);
    80200a20:	00063783          	ld	a5,0(a2)
    80200a24:	00878713          	addi	a4,a5,8
    80200a28:	00e63023          	sd	a4,0(a2)
    80200a2c:	0007b783          	ld	a5,0(a5)
    80200a30:	00f53023          	sd	a5,0(a0)
      break;
    80200a34:	00008067          	ret
    case IMAX:
      arg->i = va_arg(*ap, intmax_t);
    80200a38:	00063783          	ld	a5,0(a2)
    80200a3c:	00878713          	addi	a4,a5,8
    80200a40:	00e63023          	sd	a4,0(a2)
    80200a44:	0007b783          	ld	a5,0(a5)
    80200a48:	00f53023          	sd	a5,0(a0)
      break;
    80200a4c:	00008067          	ret
    case UMAX:
      arg->i = va_arg(*ap, uintmax_t);
    80200a50:	00063783          	ld	a5,0(a2)
    80200a54:	00878713          	addi	a4,a5,8
    80200a58:	00e63023          	sd	a4,0(a2)
    80200a5c:	0007b783          	ld	a5,0(a5)
    80200a60:	00f53023          	sd	a5,0(a0)
      break;
    80200a64:	00008067          	ret
    case PDIFF:
      arg->i = va_arg(*ap, ptrdiff_t);
    80200a68:	00063783          	ld	a5,0(a2)
    80200a6c:	00878713          	addi	a4,a5,8
    80200a70:	00e63023          	sd	a4,0(a2)
    80200a74:	0007b783          	ld	a5,0(a5)
    80200a78:	00f53023          	sd	a5,0(a0)
      break;
    80200a7c:	00008067          	ret
    case UIPTR:
      arg->i = (uintptr_t)va_arg(*ap, void *);
    80200a80:	00063783          	ld	a5,0(a2)
    80200a84:	00878713          	addi	a4,a5,8
    80200a88:	00e63023          	sd	a4,0(a2)
    80200a8c:	0007b783          	ld	a5,0(a5)
    80200a90:	00f53023          	sd	a5,0(a0)
      //   arg->f = va_arg(*ap, double);
      //   break;
      // case LDBL:
      //   arg->f = va_arg(*ap, long double);
  }
}
    80200a94:	00008067          	ret

0000000080200a98 <out>:

static void out(FILE *f, const char *s, size_t l) {
    80200a98:	ff010113          	addi	sp,sp,-16
    80200a9c:	00113423          	sd	ra,8(sp)
  f->write(f, s, l);
    80200aa0:	00053783          	ld	a5,0(a0)
    80200aa4:	000780e7          	jalr	a5
}
    80200aa8:	00813083          	ld	ra,8(sp)
    80200aac:	01010113          	addi	sp,sp,16
    80200ab0:	00008067          	ret

0000000080200ab4 <fmt_x>:
  out(f, pad, l);
}

static const char xdigits[16] = {"0123456789ABCDEF"};

static char *fmt_x(uintmax_t x, char *s, int lower) {
    80200ab4:	00050793          	mv	a5,a0
    80200ab8:	00058513          	mv	a0,a1
  for (; x; x >>= 4)
    80200abc:	0280006f          	j	80200ae4 <fmt_x+0x30>
    *--s = xdigits[(x & 15)] | lower;
    80200ac0:	00f7f693          	andi	a3,a5,15
    80200ac4:	00002717          	auipc	a4,0x2
    80200ac8:	83c70713          	addi	a4,a4,-1988 # 80202300 <xdigits>
    80200acc:	00d70733          	add	a4,a4,a3
    80200ad0:	00074703          	lbu	a4,0(a4)
    80200ad4:	fff50513          	addi	a0,a0,-1
    80200ad8:	00c76733          	or	a4,a4,a2
    80200adc:	00e50023          	sb	a4,0(a0)
  for (; x; x >>= 4)
    80200ae0:	0047d793          	srli	a5,a5,0x4
    80200ae4:	fc079ee3          	bnez	a5,80200ac0 <fmt_x+0xc>
  return s;
}
    80200ae8:	00008067          	ret

0000000080200aec <fmt_o>:

static char *fmt_o(uintmax_t x, char *s) {
    80200aec:	00050793          	mv	a5,a0
    80200af0:	00058513          	mv	a0,a1
  for (; x; x >>= 3)
    80200af4:	0180006f          	j	80200b0c <fmt_o+0x20>
    *--s = '0' + (x & 7);
    80200af8:	0077f713          	andi	a4,a5,7
    80200afc:	fff50513          	addi	a0,a0,-1
    80200b00:	03070713          	addi	a4,a4,48
    80200b04:	00e50023          	sb	a4,0(a0)
  for (; x; x >>= 3)
    80200b08:	0037d793          	srli	a5,a5,0x3
    80200b0c:	fe0796e3          	bnez	a5,80200af8 <fmt_o+0xc>
  return s;
}
    80200b10:	00008067          	ret

0000000080200b14 <fmt_u>:

static char *fmt_u(uintmax_t x, char *s) {
    80200b14:	fe010113          	addi	sp,sp,-32
    80200b18:	00113c23          	sd	ra,24(sp)
    80200b1c:	00813823          	sd	s0,16(sp)
    80200b20:	00913423          	sd	s1,8(sp)
    80200b24:	00050413          	mv	s0,a0
    80200b28:	00058493          	mv	s1,a1
  unsigned long y;
  for (; x > ULONG_MAX; x /= 10)
    *--s = '0' + x % 10;
  for (y = x; y; y /= 10)
    80200b2c:	02c0006f          	j	80200b58 <fmt_u+0x44>
    *--s = '0' + y % 10;
    80200b30:	00a00593          	li	a1,10
    80200b34:	00040513          	mv	a0,s0
    80200b38:	c29ff0ef          	jal	ra,80200760 <__umoddi3>
    80200b3c:	fff48493          	addi	s1,s1,-1
    80200b40:	0305051b          	addiw	a0,a0,48
    80200b44:	00a48023          	sb	a0,0(s1)
  for (y = x; y; y /= 10)
    80200b48:	00a00593          	li	a1,10
    80200b4c:	00040513          	mv	a0,s0
    80200b50:	bc9ff0ef          	jal	ra,80200718 <__hidden___udivdi3>
    80200b54:	00050413          	mv	s0,a0
    80200b58:	fc041ce3          	bnez	s0,80200b30 <fmt_u+0x1c>
  return s;
}
    80200b5c:	00048513          	mv	a0,s1
    80200b60:	01813083          	ld	ra,24(sp)
    80200b64:	01013403          	ld	s0,16(sp)
    80200b68:	00813483          	ld	s1,8(sp)
    80200b6c:	02010113          	addi	sp,sp,32
    80200b70:	00008067          	ret

0000000080200b74 <getint>:

static int getint(char **s) {
    80200b74:	00050813          	mv	a6,a0
  int i;
  for (i = 0; isdigit(**s); (*s)++) {
    80200b78:	00000513          	li	a0,0
    80200b7c:	0100006f          	j	80200b8c <getint+0x18>
    if (i > INT_MAX / 10 || **s - '0' > INT_MAX - 10 * i)
      i = -1;
    80200b80:	fff00513          	li	a0,-1
  for (i = 0; isdigit(**s); (*s)++) {
    80200b84:	00170713          	addi	a4,a4,1
    80200b88:	00e83023          	sd	a4,0(a6)
    80200b8c:	00083703          	ld	a4,0(a6)
    80200b90:	00074783          	lbu	a5,0(a4)
    80200b94:	0007869b          	sext.w	a3,a5
static inline int iscntrl(int c) {
  return (c >= 0 && c <= 0x1f) || c == 0x7f;
}

static inline int isdigit(int c) {
  return c >= '0' && c <= '9';
    80200b98:	fd07879b          	addiw	a5,a5,-48
    80200b9c:	00900613          	li	a2,9
    80200ba0:	04f66463          	bltu	a2,a5,80200be8 <getint+0x74>
    if (i > INT_MAX / 10 || **s - '0' > INT_MAX - 10 * i)
    80200ba4:	0cccd7b7          	lui	a5,0xcccd
    80200ba8:	ccc78793          	addi	a5,a5,-820 # ccccccc <_skernel-0x73533334>
    80200bac:	fca7cae3          	blt	a5,a0,80200b80 <getint+0xc>
    80200bb0:	fd06859b          	addiw	a1,a3,-48
    80200bb4:	0005889b          	sext.w	a7,a1
    80200bb8:	0025169b          	slliw	a3,a0,0x2
    80200bbc:	00a686bb          	addw	a3,a3,a0
    80200bc0:	0016969b          	slliw	a3,a3,0x1
    80200bc4:	40d007bb          	negw	a5,a3
    80200bc8:	80000637          	lui	a2,0x80000
    80200bcc:	fff64613          	not	a2,a2
    80200bd0:	40d606bb          	subw	a3,a2,a3
    80200bd4:	0116c663          	blt	a3,a7,80200be0 <getint+0x6c>
    else
      i = 10 * i + (**s - '0');
    80200bd8:	40f5853b          	subw	a0,a1,a5
    80200bdc:	fa9ff06f          	j	80200b84 <getint+0x10>
      i = -1;
    80200be0:	fff00513          	li	a0,-1
    80200be4:	fa1ff06f          	j	80200b84 <getint+0x10>
  }
  return i;
}
    80200be8:	00008067          	ret

0000000080200bec <pad>:
  if (fl & (LEFT_ADJ | ZERO_PAD) || l >= w)
    80200bec:	000127b7          	lui	a5,0x12
    80200bf0:	00f77733          	and	a4,a4,a5
    80200bf4:	0007071b          	sext.w	a4,a4
    80200bf8:	08071063          	bnez	a4,80200c78 <pad+0x8c>
static void pad(FILE *f, char c, size_t w, size_t l, int fl) {
    80200bfc:	ee010113          	addi	sp,sp,-288
    80200c00:	10113c23          	sd	ra,280(sp)
    80200c04:	10813823          	sd	s0,272(sp)
    80200c08:	10913423          	sd	s1,264(sp)
    80200c0c:	00050493          	mv	s1,a0
  if (fl & (LEFT_ADJ | ZERO_PAD) || l >= w)
    80200c10:	00c6ec63          	bltu	a3,a2,80200c28 <pad+0x3c>
}
    80200c14:	11813083          	ld	ra,280(sp)
    80200c18:	11013403          	ld	s0,272(sp)
    80200c1c:	10813483          	ld	s1,264(sp)
    80200c20:	12010113          	addi	sp,sp,288
    80200c24:	00008067          	ret
  l = w - l;
    80200c28:	40d60433          	sub	s0,a2,a3
  memset(pad, c, l > sizeof pad ? sizeof pad : l);
    80200c2c:	00040613          	mv	a2,s0
    80200c30:	10000793          	li	a5,256
    80200c34:	0087f463          	bgeu	a5,s0,80200c3c <pad+0x50>
    80200c38:	10000613          	li	a2,256
    80200c3c:	00010513          	mv	a0,sp
    80200c40:	c69ff0ef          	jal	ra,802008a8 <memset>
  for (; l >= sizeof pad; l -= sizeof pad)
    80200c44:	0180006f          	j	80200c5c <pad+0x70>
    out(f, pad, sizeof pad);
    80200c48:	10000613          	li	a2,256
    80200c4c:	00010593          	mv	a1,sp
    80200c50:	00048513          	mv	a0,s1
    80200c54:	e45ff0ef          	jal	ra,80200a98 <out>
  for (; l >= sizeof pad; l -= sizeof pad)
    80200c58:	f0040413          	addi	s0,s0,-256
    80200c5c:	0ff00793          	li	a5,255
    80200c60:	fe87e4e3          	bltu	a5,s0,80200c48 <pad+0x5c>
  out(f, pad, l);
    80200c64:	00040613          	mv	a2,s0
    80200c68:	00010593          	mv	a1,sp
    80200c6c:	00048513          	mv	a0,s1
    80200c70:	e29ff0ef          	jal	ra,80200a98 <out>
    80200c74:	fa1ff06f          	j	80200c14 <pad+0x28>
    80200c78:	00008067          	ret

0000000080200c7c <printf_core>:

// theoretically you can implement all other *printf functions using this one...
static int printf_core(FILE *f, const char *fmt, va_list *ap, union arg *nl_arg, int *nl_type) {
    80200c7c:	f4010113          	addi	sp,sp,-192
    80200c80:	0a113c23          	sd	ra,184(sp)
    80200c84:	0a813823          	sd	s0,176(sp)
    80200c88:	0a913423          	sd	s1,168(sp)
    80200c8c:	0b213023          	sd	s2,160(sp)
    80200c90:	09313c23          	sd	s3,152(sp)
    80200c94:	09413823          	sd	s4,144(sp)
    80200c98:	09513423          	sd	s5,136(sp)
    80200c9c:	09613023          	sd	s6,128(sp)
    80200ca0:	07713c23          	sd	s7,120(sp)
    80200ca4:	07813823          	sd	s8,112(sp)
    80200ca8:	07913423          	sd	s9,104(sp)
    80200cac:	07a13023          	sd	s10,96(sp)
    80200cb0:	05b13c23          	sd	s11,88(sp)
    80200cb4:	00050b13          	mv	s6,a0
    80200cb8:	00060d93          	mv	s11,a2
    80200cbc:	00d13823          	sd	a3,16(sp)
    80200cc0:	00e13c23          	sd	a4,24(sp)
  char *a, *z, *s = (char *)fmt;
    80200cc4:	04b13423          	sd	a1,72(sp)
  unsigned l10n = 0, fl;
  int w, p, xp;
  union arg arg;
  int argpos;
  unsigned st, ps;
  int cnt = 0, l = 0;
    80200cc8:	00000413          	li	s0,0
    80200ccc:	00000a93          	li	s5,0
  unsigned l10n = 0, fl;
    80200cd0:	00013023          	sd	zero,0(sp)
    80200cd4:	0780006f          	j	80200d4c <printf_core+0xd0>
    cnt += l;
    if (!*s)
      break;

    /* Handle literal text and %% format specifiers */
    for (a = s; *s && *s != '%'; s++)
    80200cd8:	00140413          	addi	s0,s0,1
    80200cdc:	04813423          	sd	s0,72(sp)
    80200ce0:	04813403          	ld	s0,72(sp)
    80200ce4:	00044783          	lbu	a5,0(s0)
    80200ce8:	00078e63          	beqz	a5,80200d04 <printf_core+0x88>
    80200cec:	02500713          	li	a4,37
    80200cf0:	fee794e3          	bne	a5,a4,80200cd8 <printf_core+0x5c>
    80200cf4:	0100006f          	j	80200d04 <printf_core+0x88>
      ;
    for (z = s; s[0] == '%' && s[1] == '%'; z++, s += 2)
    80200cf8:	00140413          	addi	s0,s0,1
    80200cfc:	00278793          	addi	a5,a5,2 # 12002 <_skernel-0x801edffe>
    80200d00:	04f13423          	sd	a5,72(sp)
    80200d04:	04813783          	ld	a5,72(sp)
    80200d08:	0007c683          	lbu	a3,0(a5)
    80200d0c:	02500713          	li	a4,37
    80200d10:	00e69663          	bne	a3,a4,80200d1c <printf_core+0xa0>
    80200d14:	0017c683          	lbu	a3,1(a5)
    80200d18:	fee680e3          	beq	a3,a4,80200cf8 <printf_core+0x7c>
      ;
    if (z - a > INT_MAX - cnt)
    80200d1c:	41440433          	sub	s0,s0,s4
    80200d20:	800009b7          	lui	s3,0x80000
    80200d24:	fff9c993          	not	s3,s3
    80200d28:	417989bb          	subw	s3,s3,s7
    80200d2c:	7a89c263          	blt	s3,s0,802014d0 <printf_core+0x854>
      goto overflow;
    l = z - a;
    80200d30:	0004041b          	sext.w	s0,s0
    if (f)
    80200d34:	000b0a63          	beqz	s6,80200d48 <printf_core+0xcc>
      out(f, a, l);
    80200d38:	00040613          	mv	a2,s0
    80200d3c:	000a0593          	mv	a1,s4
    80200d40:	000b0513          	mv	a0,s6
    80200d44:	d55ff0ef          	jal	ra,80200a98 <out>
    if (l)
    80200d48:	02040e63          	beqz	s0,80200d84 <printf_core+0x108>
    if (l > INT_MAX - cnt)
    80200d4c:	800007b7          	lui	a5,0x80000
    80200d50:	fff7c793          	not	a5,a5
    80200d54:	415787bb          	subw	a5,a5,s5
    80200d58:	7687c863          	blt	a5,s0,802014c8 <printf_core+0x84c>
    cnt += l;
    80200d5c:	008a8bbb          	addw	s7,s5,s0
    80200d60:	000b8a9b          	sext.w	s5,s7
    if (!*s)
    80200d64:	04813a03          	ld	s4,72(sp)
    80200d68:	000a4783          	lbu	a5,0(s4)
    80200d6c:	f6079ae3          	bnez	a5,80200ce0 <printf_core+0x64>
    pad(f, ' ', w, pl + p, fl ^ LEFT_ADJ);

    l = w;
  }

  if (f)
    80200d70:	780b1263          	bnez	s6,802014f4 <printf_core+0x878>
    return cnt;
  if (!l10n)
    80200d74:	00013783          	ld	a5,0(sp)
    80200d78:	7e078663          	beqz	a5,80201564 <printf_core+0x8e8>
    return 0;

  for (i = 1; i <= NL_ARGMAX && nl_type[i]; i++)
    80200d7c:	00100413          	li	s0,1
    80200d80:	6f80006f          	j	80201478 <printf_core+0x7fc>
    if (isdigit(s[1]) && s[2] == '$') {
    80200d84:	04813783          	ld	a5,72(sp)
    80200d88:	0017c703          	lbu	a4,1(a5) # ffffffff80000001 <_ekernel+0xfffffffeffdfa001>
    80200d8c:	00070d1b          	sext.w	s10,a4
    80200d90:	fd07071b          	addiw	a4,a4,-48
    80200d94:	00900693          	li	a3,9
    80200d98:	00e6e863          	bltu	a3,a4,80200da8 <printf_core+0x12c>
    80200d9c:	0027c683          	lbu	a3,2(a5)
    80200da0:	02400713          	li	a4,36
    80200da4:	04e68e63          	beq	a3,a4,80200e00 <printf_core+0x184>
      s++;
    80200da8:	00178793          	addi	a5,a5,1
    80200dac:	04f13423          	sd	a5,72(sp)
      argpos = -1;
    80200db0:	fff00d13          	li	s10,-1
    for (fl = 0; (unsigned)(*s - ' ') < 32 && (FLAGMASK & (1U << (*s - ' '))); s++)
    80200db4:	00000493          	li	s1,0
    80200db8:	04813703          	ld	a4,72(sp)
    80200dbc:	00074603          	lbu	a2,0(a4)
    80200dc0:	fe06079b          	addiw	a5,a2,-32 # 7fffffe0 <_skernel-0x200020>
    80200dc4:	0007869b          	sext.w	a3,a5
    80200dc8:	01f00593          	li	a1,31
    80200dcc:	04d5e663          	bltu	a1,a3,80200e18 <printf_core+0x19c>
    80200dd0:	000137b7          	lui	a5,0x13
    80200dd4:	8097879b          	addiw	a5,a5,-2039 # 12809 <_skernel-0x801ed7f7>
    80200dd8:	00d7d7bb          	srlw	a5,a5,a3
    80200ddc:	0017f793          	andi	a5,a5,1
    80200de0:	02078c63          	beqz	a5,80200e18 <printf_core+0x19c>
      fl |= 1U << (*s - ' ');
    80200de4:	00100793          	li	a5,1
    80200de8:	00d797bb          	sllw	a5,a5,a3
    80200dec:	00f4e7b3          	or	a5,s1,a5
    80200df0:	0007849b          	sext.w	s1,a5
    for (fl = 0; (unsigned)(*s - ' ') < 32 && (FLAGMASK & (1U << (*s - ' '))); s++)
    80200df4:	00170713          	addi	a4,a4,1
    80200df8:	04e13423          	sd	a4,72(sp)
    80200dfc:	fbdff06f          	j	80200db8 <printf_core+0x13c>
      argpos = s[1] - '0';
    80200e00:	fd0d0d1b          	addiw	s10,s10,-48
      s += 3;
    80200e04:	00378793          	addi	a5,a5,3
    80200e08:	04f13423          	sd	a5,72(sp)
      l10n = 1;
    80200e0c:	00100793          	li	a5,1
    80200e10:	00f13023          	sd	a5,0(sp)
      s += 3;
    80200e14:	fa1ff06f          	j	80200db4 <printf_core+0x138>
    if (*s == '*') {
    80200e18:	02a00793          	li	a5,42
    80200e1c:	0af61c63          	bne	a2,a5,80200ed4 <printf_core+0x258>
      if (isdigit(s[1]) && s[2] == '$') {
    80200e20:	00174783          	lbu	a5,1(a4)
    80200e24:	fd07861b          	addiw	a2,a5,-48
    80200e28:	00900693          	li	a3,9
    80200e2c:	00c6e863          	bltu	a3,a2,80200e3c <printf_core+0x1c0>
    80200e30:	00274683          	lbu	a3,2(a4)
    80200e34:	02400713          	li	a4,36
    80200e38:	04e68263          	beq	a3,a4,80200e7c <printf_core+0x200>
      } else if (!l10n) {
    80200e3c:	00013783          	ld	a5,0(sp)
    80200e40:	68079c63          	bnez	a5,802014d8 <printf_core+0x85c>
        w = f ? va_arg(*ap, int) : 0;
    80200e44:	080b0463          	beqz	s6,80200ecc <printf_core+0x250>
    80200e48:	000db783          	ld	a5,0(s11)
    80200e4c:	00878713          	addi	a4,a5,8
    80200e50:	00edb023          	sd	a4,0(s11)
    80200e54:	0007ac03          	lw	s8,0(a5)
        s++;
    80200e58:	04813783          	ld	a5,72(sp)
    80200e5c:	00178793          	addi	a5,a5,1
    80200e60:	04f13423          	sd	a5,72(sp)
      if (w < 0)
    80200e64:	080c5063          	bgez	s8,80200ee4 <printf_core+0x268>
        fl |= LEFT_ADJ, w = -w;
    80200e68:	000027b7          	lui	a5,0x2
    80200e6c:	00f4e7b3          	or	a5,s1,a5
    80200e70:	0007849b          	sext.w	s1,a5
    80200e74:	41800c3b          	negw	s8,s8
    80200e78:	06c0006f          	j	80200ee4 <printf_core+0x268>
        if (!f)
    80200e7c:	020b0863          	beqz	s6,80200eac <printf_core+0x230>
          w = nl_arg[s[1] - '0'].i;
    80200e80:	00379793          	slli	a5,a5,0x3
    80200e84:	e8078793          	addi	a5,a5,-384 # 1e80 <_skernel-0x801fe180>
    80200e88:	01013703          	ld	a4,16(sp)
    80200e8c:	00f707b3          	add	a5,a4,a5
    80200e90:	0007ac03          	lw	s8,0(a5)
        s += 3;
    80200e94:	04813783          	ld	a5,72(sp)
    80200e98:	00378793          	addi	a5,a5,3
    80200e9c:	04f13423          	sd	a5,72(sp)
        l10n = 1;
    80200ea0:	00100793          	li	a5,1
    80200ea4:	00f13023          	sd	a5,0(sp)
        s += 3;
    80200ea8:	fbdff06f          	j	80200e64 <printf_core+0x1e8>
          nl_type[s[1] - '0'] = INT, w = 0;
    80200eac:	00279793          	slli	a5,a5,0x2
    80200eb0:	f4078793          	addi	a5,a5,-192
    80200eb4:	01813703          	ld	a4,24(sp)
    80200eb8:	00f707b3          	add	a5,a4,a5
    80200ebc:	00900713          	li	a4,9
    80200ec0:	00e7a023          	sw	a4,0(a5)
    80200ec4:	00040c13          	mv	s8,s0
    80200ec8:	fcdff06f          	j	80200e94 <printf_core+0x218>
        w = f ? va_arg(*ap, int) : 0;
    80200ecc:	00040c13          	mv	s8,s0
    80200ed0:	f89ff06f          	j	80200e58 <printf_core+0x1dc>
    } else if ((w = getint(&s)) < 0)
    80200ed4:	04810513          	addi	a0,sp,72
    80200ed8:	c9dff0ef          	jal	ra,80200b74 <getint>
    80200edc:	00050c13          	mv	s8,a0
    80200ee0:	60054063          	bltz	a0,802014e0 <printf_core+0x864>
    if (*s == '.' && s[1] == '*') {
    80200ee4:	04813783          	ld	a5,72(sp)
    80200ee8:	0007c703          	lbu	a4,0(a5)
    80200eec:	02e00693          	li	a3,46
    80200ef0:	0ad71a63          	bne	a4,a3,80200fa4 <printf_core+0x328>
    80200ef4:	0017c603          	lbu	a2,1(a5)
    80200ef8:	02a00693          	li	a3,42
    80200efc:	0ad61463          	bne	a2,a3,80200fa4 <printf_core+0x328>
      if (isdigit(s[2]) && s[3] == '$') {
    80200f00:	0027c703          	lbu	a4,2(a5)
    80200f04:	fd07061b          	addiw	a2,a4,-48
    80200f08:	00900693          	li	a3,9
    80200f0c:	00c6e863          	bltu	a3,a2,80200f1c <printf_core+0x2a0>
    80200f10:	0037c683          	lbu	a3,3(a5)
    80200f14:	02400793          	li	a5,36
    80200f18:	02f68e63          	beq	a3,a5,80200f54 <printf_core+0x2d8>
      } else if (!l10n) {
    80200f1c:	00013783          	ld	a5,0(sp)
    80200f20:	5c079463          	bnez	a5,802014e8 <printf_core+0x86c>
        p = f ? va_arg(*ap, int) : 0;
    80200f24:	060b0c63          	beqz	s6,80200f9c <printf_core+0x320>
    80200f28:	000db783          	ld	a5,0(s11)
    80200f2c:	00878713          	addi	a4,a5,8
    80200f30:	00edb023          	sd	a4,0(s11)
    80200f34:	0007ac83          	lw	s9,0(a5)
        s += 2;
    80200f38:	04813783          	ld	a5,72(sp)
    80200f3c:	00278793          	addi	a5,a5,2
    80200f40:	04f13423          	sd	a5,72(sp)
      xp = (p >= 0);
    80200f44:	fffcc793          	not	a5,s9
    80200f48:	01f7d79b          	srliw	a5,a5,0x1f
    80200f4c:	00f13423          	sd	a5,8(sp)
    80200f50:	0640006f          	j	80200fb4 <printf_core+0x338>
        if (!f)
    80200f54:	020b0463          	beqz	s6,80200f7c <printf_core+0x300>
          p = nl_arg[s[2] - '0'].i;
    80200f58:	00371793          	slli	a5,a4,0x3
    80200f5c:	e8078793          	addi	a5,a5,-384
    80200f60:	01013703          	ld	a4,16(sp)
    80200f64:	00f707b3          	add	a5,a4,a5
    80200f68:	0007ac83          	lw	s9,0(a5)
        s += 4;
    80200f6c:	04813783          	ld	a5,72(sp)
    80200f70:	00478793          	addi	a5,a5,4
    80200f74:	04f13423          	sd	a5,72(sp)
    80200f78:	fcdff06f          	j	80200f44 <printf_core+0x2c8>
          nl_type[s[2] - '0'] = INT, p = 0;
    80200f7c:	00271793          	slli	a5,a4,0x2
    80200f80:	f4078793          	addi	a5,a5,-192
    80200f84:	01813703          	ld	a4,24(sp)
    80200f88:	00f707b3          	add	a5,a4,a5
    80200f8c:	00900713          	li	a4,9
    80200f90:	00e7a023          	sw	a4,0(a5)
    80200f94:	00040c93          	mv	s9,s0
    80200f98:	fd5ff06f          	j	80200f6c <printf_core+0x2f0>
        p = f ? va_arg(*ap, int) : 0;
    80200f9c:	00040c93          	mv	s9,s0
    80200fa0:	f99ff06f          	j	80200f38 <printf_core+0x2bc>
    } else if (*s == '.') {
    80200fa4:	02e00693          	li	a3,46
    80200fa8:	00d70a63          	beq	a4,a3,80200fbc <printf_core+0x340>
      xp = 0;
    80200fac:	00813423          	sd	s0,8(sp)
      p = -1;
    80200fb0:	fff00c93          	li	s9,-1
    st = 0;
    80200fb4:	00000913          	li	s2,0
    80200fb8:	0280006f          	j	80200fe0 <printf_core+0x364>
      s++;
    80200fbc:	00178793          	addi	a5,a5,1
    80200fc0:	04f13423          	sd	a5,72(sp)
      p = getint(&s);
    80200fc4:	04810513          	addi	a0,sp,72
    80200fc8:	badff0ef          	jal	ra,80200b74 <getint>
    80200fcc:	00050c93          	mv	s9,a0
      xp = 1;
    80200fd0:	00100793          	li	a5,1
    80200fd4:	00f13423          	sd	a5,8(sp)
    80200fd8:	fddff06f          	j	80200fb4 <printf_core+0x338>
      st = states[st] S(*s++);
    80200fdc:	00078913          	mv	s2,a5
      if (OOB(*s))
    80200fe0:	04813703          	ld	a4,72(sp)
    80200fe4:	00074783          	lbu	a5,0(a4)
    80200fe8:	fbf7879b          	addiw	a5,a5,-65
    80200fec:	03900693          	li	a3,57
    80200ff0:	50f6e063          	bltu	a3,a5,802014f0 <printf_core+0x874>
      st = states[st] S(*s++);
    80200ff4:	00170793          	addi	a5,a4,1
    80200ff8:	04f13423          	sd	a5,72(sp)
    80200ffc:	00074683          	lbu	a3,0(a4)
    80201000:	fbf6869b          	addiw	a3,a3,-65
    80201004:	02091713          	slli	a4,s2,0x20
    80201008:	02075713          	srli	a4,a4,0x20
    8020100c:	00371793          	slli	a5,a4,0x3
    80201010:	40e787b3          	sub	a5,a5,a4
    80201014:	00279793          	slli	a5,a5,0x2
    80201018:	00e787b3          	add	a5,a5,a4
    8020101c:	00179793          	slli	a5,a5,0x1
    80201020:	00001717          	auipc	a4,0x1
    80201024:	14870713          	addi	a4,a4,328 # 80202168 <states>
    80201028:	00f707b3          	add	a5,a4,a5
    8020102c:	00d787b3          	add	a5,a5,a3
    80201030:	0007c583          	lbu	a1,0(a5)
    80201034:	0005879b          	sext.w	a5,a1
    } while (st - 1 < STOP);
    80201038:	fff5869b          	addiw	a3,a1,-1
    8020103c:	00600713          	li	a4,6
    80201040:	f8d77ee3          	bgeu	a4,a3,80200fdc <printf_core+0x360>
    if (!st)
    80201044:	4e078863          	beqz	a5,80201534 <printf_core+0x8b8>
    if (st == NOARG) {
    80201048:	01800713          	li	a4,24
    8020104c:	02e78263          	beq	a5,a4,80201070 <printf_core+0x3f4>
      if (argpos >= 0) {
    80201050:	080d4863          	bltz	s10,802010e0 <printf_core+0x464>
        if (!f)
    80201054:	060b0c63          	beqz	s6,802010cc <printf_core+0x450>
          arg = nl_arg[argpos];
    80201058:	003d1793          	slli	a5,s10,0x3
    8020105c:	01013703          	ld	a4,16(sp)
    80201060:	00f707b3          	add	a5,a4,a5
    80201064:	0007b783          	ld	a5,0(a5)
    80201068:	04f13023          	sd	a5,64(sp)
    8020106c:	0080006f          	j	80201074 <printf_core+0x3f8>
      if (argpos >= 0)
    80201070:	4c0d5663          	bgez	s10,8020153c <printf_core+0x8c0>
    if (!f)
    80201074:	cc0b0ce3          	beqz	s6,80200d4c <printf_core+0xd0>
    t = s[-1];
    80201078:	04813783          	ld	a5,72(sp)
    8020107c:	fff7c783          	lbu	a5,-1(a5)
    80201080:	00078d1b          	sext.w	s10,a5
    if (fl & LEFT_ADJ)
    80201084:	00002737          	lui	a4,0x2
    80201088:	00e4f733          	and	a4,s1,a4
    8020108c:	0007071b          	sext.w	a4,a4
    80201090:	00070863          	beqz	a4,802010a0 <printf_core+0x424>
      fl &= ~ZERO_PAD;
    80201094:	ffff0737          	lui	a4,0xffff0
    80201098:	fff70713          	addi	a4,a4,-1 # fffffffffffeffff <_ekernel+0xffffffff7fde9fff>
    8020109c:	00e4f4b3          	and	s1,s1,a4
    switch (t) {
    802010a0:	fa87879b          	addiw	a5,a5,-88
    802010a4:	0ff7f693          	zext.b	a3,a5
    802010a8:	02000713          	li	a4,32
    802010ac:	2cd76c63          	bltu	a4,a3,80201384 <printf_core+0x708>
    802010b0:	00269793          	slli	a5,a3,0x2
    802010b4:	00001717          	auipc	a4,0x1
    802010b8:	01470713          	addi	a4,a4,20 # 802020c8 <_srodata+0xc8>
    802010bc:	00e787b3          	add	a5,a5,a4
    802010c0:	0007a783          	lw	a5,0(a5)
    802010c4:	00e787b3          	add	a5,a5,a4
    802010c8:	00078067          	jr	a5
          nl_type[argpos] = st;
    802010cc:	002d1793          	slli	a5,s10,0x2
    802010d0:	01813703          	ld	a4,24(sp)
    802010d4:	00f707b3          	add	a5,a4,a5
    802010d8:	00b7a023          	sw	a1,0(a5)
    802010dc:	f99ff06f          	j	80201074 <printf_core+0x3f8>
      } else if (f)
    802010e0:	460b0263          	beqz	s6,80201544 <printf_core+0x8c8>
        pop_arg(&arg, st, ap);
    802010e4:	000d8613          	mv	a2,s11
    802010e8:	04010513          	addi	a0,sp,64
    802010ec:	ffcff0ef          	jal	ra,802008e8 <pop_arg>
    802010f0:	f85ff06f          	j	80201074 <printf_core+0x3f8>
        switch (ps) {
    802010f4:	00600793          	li	a5,6
    802010f8:	c527eae3          	bltu	a5,s2,80200d4c <printf_core+0xd0>
    802010fc:	00291793          	slli	a5,s2,0x2
    80201100:	00001717          	auipc	a4,0x1
    80201104:	04c70713          	addi	a4,a4,76 # 8020214c <_srodata+0x14c>
    80201108:	00e787b3          	add	a5,a5,a4
    8020110c:	0007a783          	lw	a5,0(a5)
    80201110:	00e787b3          	add	a5,a5,a4
    80201114:	00078067          	jr	a5
            *(int *)arg.p = cnt;
    80201118:	04013783          	ld	a5,64(sp)
    8020111c:	0177a023          	sw	s7,0(a5)
            break;
    80201120:	c2dff06f          	j	80200d4c <printf_core+0xd0>
            *(long *)arg.p = cnt;
    80201124:	04013783          	ld	a5,64(sp)
    80201128:	0157b023          	sd	s5,0(a5)
            break;
    8020112c:	c21ff06f          	j	80200d4c <printf_core+0xd0>
            *(long long *)arg.p = cnt;
    80201130:	04013783          	ld	a5,64(sp)
    80201134:	0157b023          	sd	s5,0(a5)
            break;
    80201138:	c15ff06f          	j	80200d4c <printf_core+0xd0>
            *(unsigned short *)arg.p = cnt;
    8020113c:	04013783          	ld	a5,64(sp)
    80201140:	01579023          	sh	s5,0(a5)
            break;
    80201144:	c09ff06f          	j	80200d4c <printf_core+0xd0>
            *(unsigned char *)arg.p = cnt;
    80201148:	04013783          	ld	a5,64(sp)
    8020114c:	01578023          	sb	s5,0(a5)
            break;
    80201150:	bfdff06f          	j	80200d4c <printf_core+0xd0>
            *(size_t *)arg.p = cnt;
    80201154:	04013783          	ld	a5,64(sp)
    80201158:	0157b023          	sd	s5,0(a5)
            break;
    8020115c:	bf1ff06f          	j	80200d4c <printf_core+0xd0>
            *(uintmax_t *)arg.p = cnt;
    80201160:	04013783          	ld	a5,64(sp)
    80201164:	0157b023          	sd	s5,0(a5)
        continue;
    80201168:	be5ff06f          	j	80200d4c <printf_core+0xd0>
        p = MAX((size_t)p, 2 * sizeof(void *));
    8020116c:	01000793          	li	a5,16
    80201170:	00fcf463          	bgeu	s9,a5,80201178 <printf_core+0x4fc>
    80201174:	01000c93          	li	s9,16
    80201178:	000c8c9b          	sext.w	s9,s9
        fl |= ALT_FORM;
    8020117c:	0084e493          	ori	s1,s1,8
        t = 'x';
    80201180:	07800d13          	li	s10,120
        a = fmt_x(arg.i, z, t & 32);
    80201184:	020d7613          	andi	a2,s10,32
    80201188:	04010593          	addi	a1,sp,64
    8020118c:	04013503          	ld	a0,64(sp)
    80201190:	925ff0ef          	jal	ra,80200ab4 <fmt_x>
    80201194:	00050a13          	mv	s4,a0
        if (arg.i && (fl & ALT_FORM))
    80201198:	04013783          	ld	a5,64(sp)
    8020119c:	12078263          	beqz	a5,802012c0 <printf_core+0x644>
    802011a0:	0084f793          	andi	a5,s1,8
    802011a4:	12078463          	beqz	a5,802012cc <printf_core+0x650>
          prefix += (t >> 4), pl = 2;
    802011a8:	004d5d13          	srli	s10,s10,0x4
    802011ac:	00001797          	auipc	a5,0x1
    802011b0:	f0478793          	addi	a5,a5,-252 # 802020b0 <_srodata+0xb0>
    802011b4:	00fd0d33          	add	s10,s10,a5
    802011b8:	00200413          	li	s0,2
    802011bc:	0980006f          	j	80201254 <printf_core+0x5d8>
            a = fmt_o(arg.i, z);
    802011c0:	04010593          	addi	a1,sp,64
    802011c4:	04013503          	ld	a0,64(sp)
    802011c8:	925ff0ef          	jal	ra,80200aec <fmt_o>
    802011cc:	00050a13          	mv	s4,a0
            if ((fl & ALT_FORM) && p < z - a + 1)
    802011d0:	0084f793          	andi	a5,s1,8
    802011d4:	10078263          	beqz	a5,802012d8 <printf_core+0x65c>
    802011d8:	04010793          	addi	a5,sp,64
    802011dc:	40a787b3          	sub	a5,a5,a0
    802011e0:	1197c263          	blt	a5,s9,802012e4 <printf_core+0x668>
              p = z - a + 1;
    802011e4:	00178c9b          	addiw	s9,a5,1
    prefix = "-+   0X0x";
    802011e8:	00001d17          	auipc	s10,0x1
    802011ec:	ec8d0d13          	addi	s10,s10,-312 # 802020b0 <_srodata+0xb0>
    802011f0:	0640006f          	j	80201254 <printf_core+0x5d8>
            if (arg.i > INTMAX_MAX) {
    802011f4:	04013783          	ld	a5,64(sp)
    802011f8:	0207c663          	bltz	a5,80201224 <printf_core+0x5a8>
            } else if (fl & MARK_POS) {
    802011fc:	000017b7          	lui	a5,0x1
    80201200:	80078793          	addi	a5,a5,-2048 # 800 <_skernel-0x801ff800>
    80201204:	00f4f7b3          	and	a5,s1,a5
    80201208:	08079e63          	bnez	a5,802012a4 <printf_core+0x628>
            } else if (fl & PAD_POS) {
    8020120c:	0014f793          	andi	a5,s1,1
    80201210:	0a078263          	beqz	a5,802012b4 <printf_core+0x638>
            pl = 1;
    80201214:	00100413          	li	s0,1
              prefix += 2;
    80201218:	00001d17          	auipc	s10,0x1
    8020121c:	e9ad0d13          	addi	s10,s10,-358 # 802020b2 <_srodata+0xb2>
    80201220:	0240006f          	j	80201244 <printf_core+0x5c8>
              arg.i = -arg.i;
    80201224:	40f007b3          	neg	a5,a5
    80201228:	04f13023          	sd	a5,64(sp)
            pl = 1;
    8020122c:	00100413          	li	s0,1
    prefix = "-+   0X0x";
    80201230:	00001d17          	auipc	s10,0x1
    80201234:	e80d0d13          	addi	s10,s10,-384 # 802020b0 <_srodata+0xb0>
    80201238:	00c0006f          	j	80201244 <printf_core+0x5c8>
    switch (t) {
    8020123c:	00001d17          	auipc	s10,0x1
    80201240:	e74d0d13          	addi	s10,s10,-396 # 802020b0 <_srodata+0xb0>
            a = fmt_u(arg.i, z);
    80201244:	04010593          	addi	a1,sp,64
    80201248:	04013503          	ld	a0,64(sp)
    8020124c:	8c9ff0ef          	jal	ra,80200b14 <fmt_u>
    80201250:	00050a13          	mv	s4,a0
        if (xp && p < 0)
    80201254:	00813783          	ld	a5,8(sp)
    80201258:	00078463          	beqz	a5,80201260 <printf_core+0x5e4>
    8020125c:	2e0cc863          	bltz	s9,8020154c <printf_core+0x8d0>
        if (xp)
    80201260:	00813783          	ld	a5,8(sp)
    80201264:	00078863          	beqz	a5,80201274 <printf_core+0x5f8>
          fl &= ~ZERO_PAD;
    80201268:	ffff07b7          	lui	a5,0xffff0
    8020126c:	fff78793          	addi	a5,a5,-1 # fffffffffffeffff <_ekernel+0xffffffff7fde9fff>
    80201270:	00f4f4b3          	and	s1,s1,a5
        if (!arg.i && !p) {
    80201274:	04013703          	ld	a4,64(sp)
    80201278:	00071463          	bnez	a4,80201280 <printf_core+0x604>
    8020127c:	1c0c8c63          	beqz	s9,80201454 <printf_core+0x7d8>
        p = MAX(p, z - a + !arg.i);
    80201280:	04010793          	addi	a5,sp,64
    80201284:	414787b3          	sub	a5,a5,s4
    80201288:	00173713          	seqz	a4,a4
    8020128c:	00e787b3          	add	a5,a5,a4
    80201290:	00fcd463          	bge	s9,a5,80201298 <printf_core+0x61c>
    80201294:	00078c93          	mv	s9,a5
    80201298:	000c8c9b          	sext.w	s9,s9
    z = buf + sizeof(buf);
    8020129c:	04010913          	addi	s2,sp,64
        break;
    802012a0:	0f00006f          	j	80201390 <printf_core+0x714>
            pl = 1;
    802012a4:	00100413          	li	s0,1
              prefix++;
    802012a8:	00001d17          	auipc	s10,0x1
    802012ac:	e09d0d13          	addi	s10,s10,-503 # 802020b1 <_srodata+0xb1>
    802012b0:	f95ff06f          	j	80201244 <printf_core+0x5c8>
    prefix = "-+   0X0x";
    802012b4:	00001d17          	auipc	s10,0x1
    802012b8:	dfcd0d13          	addi	s10,s10,-516 # 802020b0 <_srodata+0xb0>
    802012bc:	f89ff06f          	j	80201244 <printf_core+0x5c8>
    802012c0:	00001d17          	auipc	s10,0x1
    802012c4:	df0d0d13          	addi	s10,s10,-528 # 802020b0 <_srodata+0xb0>
    802012c8:	f8dff06f          	j	80201254 <printf_core+0x5d8>
    802012cc:	00001d17          	auipc	s10,0x1
    802012d0:	de4d0d13          	addi	s10,s10,-540 # 802020b0 <_srodata+0xb0>
    802012d4:	f81ff06f          	j	80201254 <printf_core+0x5d8>
    802012d8:	00001d17          	auipc	s10,0x1
    802012dc:	dd8d0d13          	addi	s10,s10,-552 # 802020b0 <_srodata+0xb0>
    802012e0:	f75ff06f          	j	80201254 <printf_core+0x5d8>
    802012e4:	00001d17          	auipc	s10,0x1
    802012e8:	dccd0d13          	addi	s10,s10,-564 # 802020b0 <_srodata+0xb0>
    802012ec:	f69ff06f          	j	80201254 <printf_core+0x5d8>
        *(a = z - (p = 1)) = arg.i;
    802012f0:	04013783          	ld	a5,64(sp)
    802012f4:	02f10fa3          	sb	a5,63(sp)
        fl &= ~ZERO_PAD;
    802012f8:	ffff07b7          	lui	a5,0xffff0
    802012fc:	fff78793          	addi	a5,a5,-1 # fffffffffffeffff <_ekernel+0xffffffff7fde9fff>
    80201300:	00f4f4b3          	and	s1,s1,a5
    prefix = "-+   0X0x";
    80201304:	00001d17          	auipc	s10,0x1
    80201308:	dacd0d13          	addi	s10,s10,-596 # 802020b0 <_srodata+0xb0>
        *(a = z - (p = 1)) = arg.i;
    8020130c:	00100c93          	li	s9,1
    z = buf + sizeof(buf);
    80201310:	04010913          	addi	s2,sp,64
        *(a = z - (p = 1)) = arg.i;
    80201314:	03f10a13          	addi	s4,sp,63
        break;
    80201318:	0780006f          	j	80201390 <printf_core+0x714>
        a = arg.p ? arg.p : "(null)";
    8020131c:	04013a03          	ld	s4,64(sp)
    80201320:	020a0e63          	beqz	s4,8020135c <printf_core+0x6e0>
        z = a + strnlen(a, p < 0 ? INT_MAX : p);
    80201324:	040cc263          	bltz	s9,80201368 <printf_core+0x6ec>
    80201328:	000c8593          	mv	a1,s9
    8020132c:	000a0513          	mv	a0,s4
    80201330:	d94ff0ef          	jal	ra,802008c4 <strnlen>
    80201334:	00050793          	mv	a5,a0
    80201338:	00aa0933          	add	s2,s4,a0
        if (p < 0 && *z)
    8020133c:	020ccc63          	bltz	s9,80201374 <printf_core+0x6f8>
        p = z - a;
    80201340:	00078c9b          	sext.w	s9,a5
        fl &= ~ZERO_PAD;
    80201344:	ffff07b7          	lui	a5,0xffff0
    80201348:	fff78793          	addi	a5,a5,-1 # fffffffffffeffff <_ekernel+0xffffffff7fde9fff>
    8020134c:	00f4f4b3          	and	s1,s1,a5
    prefix = "-+   0X0x";
    80201350:	00001d17          	auipc	s10,0x1
    80201354:	d60d0d13          	addi	s10,s10,-672 # 802020b0 <_srodata+0xb0>
        break;
    80201358:	0380006f          	j	80201390 <printf_core+0x714>
        a = arg.p ? arg.p : "(null)";
    8020135c:	00001a17          	auipc	s4,0x1
    80201360:	d64a0a13          	addi	s4,s4,-668 # 802020c0 <_srodata+0xc0>
    80201364:	fc1ff06f          	j	80201324 <printf_core+0x6a8>
        z = a + strnlen(a, p < 0 ? INT_MAX : p);
    80201368:	800005b7          	lui	a1,0x80000
    8020136c:	fff5c593          	not	a1,a1
    80201370:	fbdff06f          	j	8020132c <printf_core+0x6b0>
        if (p < 0 && *z)
    80201374:	00094703          	lbu	a4,0(s2)
    80201378:	fc0704e3          	beqz	a4,80201340 <printf_core+0x6c4>
inval:
  // errno = EINVAL;
  // return -1;
overflow:
  // errno = EOVERFLOW;
  return -1;
    8020137c:	fff00a93          	li	s5,-1
    80201380:	1740006f          	j	802014f4 <printf_core+0x878>
    switch (t) {
    80201384:	00001d17          	auipc	s10,0x1
    80201388:	d2cd0d13          	addi	s10,s10,-724 # 802020b0 <_srodata+0xb0>
    8020138c:	04010913          	addi	s2,sp,64
    if (p < z - a)
    80201390:	41490933          	sub	s2,s2,s4
    80201394:	012cd463          	bge	s9,s2,8020139c <printf_core+0x720>
      p = z - a;
    80201398:	00090c9b          	sext.w	s9,s2
    if (p > INT_MAX - pl)
    8020139c:	800007b7          	lui	a5,0x80000
    802013a0:	fff7c793          	not	a5,a5
    802013a4:	408787bb          	subw	a5,a5,s0
    802013a8:	1b97c663          	blt	a5,s9,80201554 <printf_core+0x8d8>
    if (w < pl + p)
    802013ac:	008c8bbb          	addw	s7,s9,s0
    802013b0:	017c5463          	bge	s8,s7,802013b8 <printf_core+0x73c>
      w = pl + p;
    802013b4:	000b8c13          	mv	s8,s7
    if (w > INT_MAX - cnt)
    802013b8:	1b89c263          	blt	s3,s8,8020155c <printf_core+0x8e0>
    pad(f, ' ', w, pl + p, fl);
    802013bc:	00048713          	mv	a4,s1
    802013c0:	000b8693          	mv	a3,s7
    802013c4:	000c0613          	mv	a2,s8
    802013c8:	02000593          	li	a1,32
    802013cc:	000b0513          	mv	a0,s6
    802013d0:	81dff0ef          	jal	ra,80200bec <pad>
    out(f, prefix, pl);
    802013d4:	00040613          	mv	a2,s0
    802013d8:	000d0593          	mv	a1,s10
    802013dc:	000b0513          	mv	a0,s6
    802013e0:	eb8ff0ef          	jal	ra,80200a98 <out>
    pad(f, '0', w, pl + p, fl ^ ZERO_PAD);
    802013e4:	00010737          	lui	a4,0x10
    802013e8:	00e4c733          	xor	a4,s1,a4
    802013ec:	0007071b          	sext.w	a4,a4
    802013f0:	000b8693          	mv	a3,s7
    802013f4:	000c0613          	mv	a2,s8
    802013f8:	03000593          	li	a1,48
    802013fc:	000b0513          	mv	a0,s6
    80201400:	fecff0ef          	jal	ra,80200bec <pad>
    pad(f, '0', p, z - a, 0);
    80201404:	00000713          	li	a4,0
    80201408:	00090693          	mv	a3,s2
    8020140c:	000c8613          	mv	a2,s9
    80201410:	03000593          	li	a1,48
    80201414:	000b0513          	mv	a0,s6
    80201418:	fd4ff0ef          	jal	ra,80200bec <pad>
    out(f, a, z - a);
    8020141c:	00090613          	mv	a2,s2
    80201420:	000a0593          	mv	a1,s4
    80201424:	000b0513          	mv	a0,s6
    80201428:	e70ff0ef          	jal	ra,80200a98 <out>
    pad(f, ' ', w, pl + p, fl ^ LEFT_ADJ);
    8020142c:	000027b7          	lui	a5,0x2
    80201430:	00f4c733          	xor	a4,s1,a5
    80201434:	0007071b          	sext.w	a4,a4
    80201438:	000b8693          	mv	a3,s7
    8020143c:	000c0613          	mv	a2,s8
    80201440:	02000593          	li	a1,32
    80201444:	000b0513          	mv	a0,s6
    80201448:	fa4ff0ef          	jal	ra,80200bec <pad>
    l = w;
    8020144c:	000c0413          	mv	s0,s8
    80201450:	8fdff06f          	j	80200d4c <printf_core+0xd0>
    z = buf + sizeof(buf);
    80201454:	04010913          	addi	s2,sp,64
          a = z;
    80201458:	00090a13          	mv	s4,s2
    8020145c:	f35ff06f          	j	80201390 <printf_core+0x714>
    pop_arg(nl_arg + i, nl_type[i], ap);
    80201460:	00341513          	slli	a0,s0,0x3
    80201464:	000d8613          	mv	a2,s11
    80201468:	01013783          	ld	a5,16(sp)
    8020146c:	00a78533          	add	a0,a5,a0
    80201470:	c78ff0ef          	jal	ra,802008e8 <pop_arg>
  for (i = 1; i <= NL_ARGMAX && nl_type[i]; i++)
    80201474:	00140413          	addi	s0,s0,1
    80201478:	00900793          	li	a5,9
    8020147c:	0287e063          	bltu	a5,s0,8020149c <printf_core+0x820>
    80201480:	00241793          	slli	a5,s0,0x2
    80201484:	01813703          	ld	a4,24(sp)
    80201488:	00f707b3          	add	a5,a4,a5
    8020148c:	0007a583          	lw	a1,0(a5) # 2000 <_skernel-0x801fe000>
    80201490:	fc0598e3          	bnez	a1,80201460 <printf_core+0x7e4>
    80201494:	0080006f          	j	8020149c <printf_core+0x820>
  for (; i <= NL_ARGMAX && !nl_type[i]; i++)
    80201498:	00140413          	addi	s0,s0,1
    8020149c:	00900793          	li	a5,9
    802014a0:	0087ec63          	bltu	a5,s0,802014b8 <printf_core+0x83c>
    802014a4:	00241793          	slli	a5,s0,0x2
    802014a8:	01813703          	ld	a4,24(sp)
    802014ac:	00f707b3          	add	a5,a4,a5
    802014b0:	0007a783          	lw	a5,0(a5)
    802014b4:	fe0782e3          	beqz	a5,80201498 <printf_core+0x81c>
  if (i <= NL_ARGMAX)
    802014b8:	00900793          	li	a5,9
    802014bc:	0a87f863          	bgeu	a5,s0,8020156c <printf_core+0x8f0>
  return 1;
    802014c0:	00100a93          	li	s5,1
    802014c4:	0300006f          	j	802014f4 <printf_core+0x878>
  return -1;
    802014c8:	fff00a93          	li	s5,-1
    802014cc:	0280006f          	j	802014f4 <printf_core+0x878>
    802014d0:	fff00a93          	li	s5,-1
    802014d4:	0200006f          	j	802014f4 <printf_core+0x878>
    802014d8:	fff00a93          	li	s5,-1
    802014dc:	0180006f          	j	802014f4 <printf_core+0x878>
    802014e0:	fff00a93          	li	s5,-1
    802014e4:	0100006f          	j	802014f4 <printf_core+0x878>
    802014e8:	fff00a93          	li	s5,-1
    802014ec:	0080006f          	j	802014f4 <printf_core+0x878>
    802014f0:	fff00a93          	li	s5,-1
}
    802014f4:	000a8513          	mv	a0,s5
    802014f8:	0b813083          	ld	ra,184(sp)
    802014fc:	0b013403          	ld	s0,176(sp)
    80201500:	0a813483          	ld	s1,168(sp)
    80201504:	0a013903          	ld	s2,160(sp)
    80201508:	09813983          	ld	s3,152(sp)
    8020150c:	09013a03          	ld	s4,144(sp)
    80201510:	08813a83          	ld	s5,136(sp)
    80201514:	08013b03          	ld	s6,128(sp)
    80201518:	07813b83          	ld	s7,120(sp)
    8020151c:	07013c03          	ld	s8,112(sp)
    80201520:	06813c83          	ld	s9,104(sp)
    80201524:	06013d03          	ld	s10,96(sp)
    80201528:	05813d83          	ld	s11,88(sp)
    8020152c:	0c010113          	addi	sp,sp,192
    80201530:	00008067          	ret
  return -1;
    80201534:	fff00a93          	li	s5,-1
    80201538:	fbdff06f          	j	802014f4 <printf_core+0x878>
    8020153c:	fff00a93          	li	s5,-1
    80201540:	fb5ff06f          	j	802014f4 <printf_core+0x878>
        return 0;
    80201544:	00040a93          	mv	s5,s0
    80201548:	fadff06f          	j	802014f4 <printf_core+0x878>
  return -1;
    8020154c:	fff00a93          	li	s5,-1
    80201550:	fa5ff06f          	j	802014f4 <printf_core+0x878>
    80201554:	fff00a93          	li	s5,-1
    80201558:	f9dff06f          	j	802014f4 <printf_core+0x878>
    8020155c:	fff00a93          	li	s5,-1
    80201560:	f95ff06f          	j	802014f4 <printf_core+0x878>
    return 0;
    80201564:	00000a93          	li	s5,0
    80201568:	f8dff06f          	j	802014f4 <printf_core+0x878>
  return -1;
    8020156c:	fff00a93          	li	s5,-1
    80201570:	f85ff06f          	j	802014f4 <printf_core+0x878>

0000000080201574 <vfprintf>:
  return ret;
}

#else

int vfprintf(FILE *restrict f, const char *restrict fmt, va_list ap) {
    80201574:	f5010113          	addi	sp,sp,-176
    80201578:	0a113423          	sd	ra,168(sp)
    8020157c:	0a813023          	sd	s0,160(sp)
    80201580:	08913c23          	sd	s1,152(sp)
    80201584:	00050413          	mv	s0,a0
    80201588:	00058493          	mv	s1,a1
    8020158c:	00c13423          	sd	a2,8(sp)
  int nl_type[NL_ARGMAX + 1] = {0};
    80201590:	06013423          	sd	zero,104(sp)
    80201594:	06013823          	sd	zero,112(sp)
    80201598:	06013c23          	sd	zero,120(sp)
    8020159c:	08013023          	sd	zero,128(sp)
    802015a0:	08013423          	sd	zero,136(sp)
  union arg nl_arg[NL_ARGMAX + 1];

  // preprocess nl arguments
  va_list ap2;
  va_copy(ap2, ap);
    802015a4:	00c13823          	sd	a2,16(sp)
  int ret = printf_core(0, fmt, &ap2, nl_arg, nl_type);
    802015a8:	06810713          	addi	a4,sp,104
    802015ac:	01810693          	addi	a3,sp,24
    802015b0:	01010613          	addi	a2,sp,16
    802015b4:	00000513          	li	a0,0
    802015b8:	ec4ff0ef          	jal	ra,80200c7c <printf_core>
  va_end(ap2);

  if (ret < 0) {
    802015bc:	00054e63          	bltz	a0,802015d8 <vfprintf+0x64>
    return ret;
  }
  return printf_core(f, fmt, &ap, nl_arg, nl_type);
    802015c0:	06810713          	addi	a4,sp,104
    802015c4:	01810693          	addi	a3,sp,24
    802015c8:	00810613          	addi	a2,sp,8
    802015cc:	00048593          	mv	a1,s1
    802015d0:	00040513          	mv	a0,s0
    802015d4:	ea8ff0ef          	jal	ra,80200c7c <printf_core>
}
    802015d8:	0a813083          	ld	ra,168(sp)
    802015dc:	0a013403          	ld	s0,160(sp)
    802015e0:	09813483          	ld	s1,152(sp)
    802015e4:	0b010113          	addi	sp,sp,176
    802015e8:	00008067          	ret
