#include <printk.h>
#include <stdint.h>

#define S_TIMER_INT 0x8000000000000005UL

void clock_set_next_event(void);
extern void do_timer(void);

void trap_handler(uint64_t scause, uint64_t sepc) {
    if (scause == S_TIMER_INT) {
        clock_set_next_event();
        do_timer();
        return;
    }

    printk("Unhandled trap: scause=%lx, sepc=%lx\n", scause, sepc);
    clock_set_next_event();
}
