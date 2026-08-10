#ifndef __PRIVATE_KDEFS_H__
#define __PRIVATE_KDEFS_H__

#define PHY_START 0x80000000
#define PHY_SIZE 0x8000000
#define PHY_END (PHY_START + PHY_SIZE)

#define OPENSBI_SIZE 0x200000

#define VM_START 0xffffffe000000000
#define VM_END 0xffffffff00000000
#define VM_SIZE (VM_END - VM_START)

#define PA2VA_OFFSET (VM_START - PHY_START)

#define PGSIZE 0x1000
#define PGROUNDDOWN(addr) ((addr) & ~(PGSIZE - 1))
#define PGROUNDUP(addr) PGROUNDDOWN((addr) + PGSIZE - 1)

#define TIMECLOCK 200000

#endif
