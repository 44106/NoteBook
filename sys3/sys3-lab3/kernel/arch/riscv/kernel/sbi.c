#include <sbi.h>
#include <stdint.h>

struct sbiret sbi_ecall(uint64_t eid, uint64_t fid,
                        uint64_t arg0, uint64_t arg1, uint64_t arg2,
                        uint64_t arg3, uint64_t arg4, uint64_t arg5) {
    struct sbiret ret;

    asm volatile(
        "mv a0, %2\n"
        "mv a1, %3\n"
        "mv a2, %4\n"
        "mv a3, %5\n"
        "mv a4, %6\n"
        "mv a5, %7\n"
        "mv a6, %8\n"
        "mv a7, %9\n"
        "ecall\n"
        "mv %0, a0\n"
        "mv %1, a1\n"
        : "=r"(ret.error), "=r"(ret.value)
        : "r"(arg0), "r"(arg1), "r"(arg2), "r"(arg3),
          "r"(arg4), "r"(arg5), "r"(fid), "r"(eid)
        : "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "memory");

    return ret;
}
