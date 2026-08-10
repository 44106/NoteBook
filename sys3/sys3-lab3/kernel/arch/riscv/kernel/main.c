#include <printk.h>
#include <sbi.h>
#include <private_kdefs.h>
extern void task_init(void);
_Noreturn void start_kernel(void) {
    task_init();
    // 等待第一次时钟中断
    while (1)
        ;
}
