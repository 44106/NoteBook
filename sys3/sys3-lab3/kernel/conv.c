#include "conv.h"

//typedef unsigned long long int size_t;
uint64_t* CONV_BASE = (uint64_t*)0x10001000L;
const size_t CONV_KERNEL_OFFSET = 0;
const size_t CONV_DATA_OFFSET = 1;
const size_t CONV_RESULT_LO_OFFSET = 0;
const size_t CONV_RESULT_HI_OFFSET = 1;
const size_t CONV_STATE_OFFSET = 2;
const unsigned char READY_MASK = 0b01;
const size_t CONV_ELEMENT_LEN = 4;

uint64_t* MISC_BASE = (uint64_t*)0x10002000L;
const size_t MISC_TIME_OFFSET = 0;

uint64_t get_time(void) {
    return MISC_BASE[MISC_TIME_OFFSET];
}

void conv_compute(const uint64_t* data_array, size_t data_len, const uint64_t* kernel_array, size_t kernel_len, uint64_t* dest) {
    // fill the code
    for (int i = 0; i < kernel_len; i++) {
        CONV_BASE[CONV_KERNEL_OFFSET] = kernel_array[i];
    }
    for (int i = 0; i < data_len + 6; i++) {
        if (i - 3 < 0 || i - 3 >= data_len) CONV_BASE[CONV_DATA_OFFSET] = 0;
        else CONV_BASE[CONV_DATA_OFFSET] = data_array[i - 3];
        while ((CONV_BASE[CONV_STATE_OFFSET] & READY_MASK) == 0) {}
        if (i >= 3) {
            dest[(i - 3) << 1] = CONV_BASE[CONV_RESULT_HI_OFFSET];
            dest[((i - 3) << 1) + 1] = CONV_BASE[CONV_RESULT_LO_OFFSET];
        }
    }
}

void mul_compute(const uint64_t* data_array, size_t data_len, const uint64_t* kernel_array, size_t kernel_len, uint64_t* dest) {
    // fill the code
    for (int i = 0; i < data_len + kernel_len - 1; i++) {
        __uint128_t acc = 0;
        for (int j = 0; j < kernel_len; j++) {
            if (i + j - 3 >= 0 && i + j - 3 < data_len) {
                unsigned __int128 res = 0;
                unsigned __int128 temp_a = data_array[i + j - 3];
                uint64_t temp_b = kernel_array[j];
                while (temp_b > 0) {
                    if (temp_b & 1) {
                        res += temp_a;
                    }
                    temp_a <<= 1;
                    temp_b >>= 1;
                }
                acc += res;
            }
        }
        dest[i << 1] = (uint64_t)(acc >> 64);
        dest[(i << 1) + 1] = (uint64_t)(acc);
    }
}