#ifndef __VM_H__
#define __VM_H__

#include <stdint.h>

void setup_vm(void);
void setup_vm_final(void);
void create_mapping(uint64_t *pgtbl, void *va, void *pa,
                    uint64_t sz, uint64_t perm);

#endif
