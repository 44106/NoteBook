#include <private_kdefs.h>
#include <sbi.h>
#include <stdint.h>

void clock_set_next_event(void) {
    uint64_t now;
    uint64_t next;

    asm volatile("rdtime %0" : "=r"(now));
    next = now + TIMECLOCK;
    sbi_ecall(0x54494d45, 0, next, 0, 0, 0, 0, 0);
}
