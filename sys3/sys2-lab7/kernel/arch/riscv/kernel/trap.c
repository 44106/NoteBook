#include <stdint.h>
#include <printk.h>

void clock_set_next_event(void);
extern void do_timer(void);
void trap_handler(uint64_t scause, uint64_t sepc) {
  // 根据 scause 判断 trap 类型
  // 如果是 Supervisor Timer Interrupt：
  // - 打印输出相关信息
  // - 调用 clock_set_next_event 设置下一次时钟中断
  // 其他类型的 trap 可以直接忽略，推荐打印出来供以后调试
	if (scause == 0x8000000000000005) {
		clock_set_next_event();
		do_timer();
	}
	else {
		printk("Unhandled trap: scause=%lx, sepc=%lx\n", scause, sepc);
		clock_set_next_event();
	}
}
