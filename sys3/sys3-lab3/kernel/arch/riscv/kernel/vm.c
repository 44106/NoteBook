#include <mm.h>
#include <printk.h>
#include <sbi.h>
#include <string.h>
#include <vm.h>
#define SATP_SV39 (8UL << 60)
#define PTE_V (1UL << 0)
#define PTE_R (1UL << 1)
#define PTE_W (1UL << 2)
#define PTE_X (1UL << 3)
#define PTE_U (1UL << 4)
#define PTE_G (1UL << 5)
#define PTE_A (1UL << 6)
#define PTE_D (1UL << 7)
#define PA2PTE(pa) ((((uint64_t)(pa)) >> 12) << 10)
#define PTE2PA(pte) ((((uint64_t)(pte)) >> 10) << 12)
#define VPN2(va) ((((uint64_t)(va)) >> 30) & 0x1ff)
#define VPN1(va) ((((uint64_t)(va)) >> 21) & 0x1ff)
#define VPN0(va) ((((uint64_t)(va)) >> 12) & 0x1ff)
extern char _stext[];
extern char _srodata[];
extern char _sdata[];
uint64_t early_pgtbl[PGSIZE / 8] __attribute__((__aligned__(PGSIZE)));
uint64_t swapper_pg_dir[PGSIZE / 8] __attribute__((__aligned__(PGSIZE)));

void setup_vm(void) {
    uint64_t pte;
    memset(early_pgtbl, 0, PGSIZE);
    pte = PA2PTE(PHY_START) | PTE_V | PTE_R | PTE_W | PTE_X | PTE_A | PTE_D;
    early_pgtbl[VPN2(VM_START)] = pte;
}

void create_mapping(uint64_t *pgtbl, void *va, void *pa,
                    uint64_t sz, uint64_t perm) {
    uint64_t va_start = (uint64_t)va;
    uint64_t pa_start = (uint64_t)pa;
    uint64_t i;

    printk("pgtbl = %#lx: map [%#lx, %#lx) -> [%#lx, %#lx), perm = %#lx, size = %lu\n",
           VA2PA(pgtbl), va_start, va_start + sz, pa_start, pa_start + sz, perm, sz);

    for (i = 0; i < sz; i += PGSIZE) {
        uint64_t now_va = va_start + i;
        uint64_t now_pa = pa_start + i;
        uint64_t *pmd;
        uint64_t *pte;

        if ((pgtbl[VPN2(now_va)] & PTE_V) == 0) {
            uint64_t *page = (uint64_t *)alloc_page();
            memset(page, 0, PGSIZE);
            pgtbl[VPN2(now_va)] = PA2PTE(VA2PA(page)) | PTE_V;
        }

        pmd = (uint64_t *)PA2VA(PTE2PA(pgtbl[VPN2(now_va)]));
        if ((pmd[VPN1(now_va)] & PTE_V) == 0) {
            uint64_t *page = (uint64_t *)alloc_page();
            memset(page, 0, PGSIZE);
            pmd[VPN1(now_va)] = PA2PTE(VA2PA(page)) | PTE_V;
        }

        pte = (uint64_t *)PA2VA(PTE2PA(pmd[VPN1(now_va)]));
        pte[VPN0(now_va)] = PA2PTE(now_pa) | perm | PTE_V | PTE_A | PTE_D;
    }
}

void setup_vm_final(void) {
    uint64_t satp_val;
    memset(swapper_pg_dir, 0, PGSIZE);
    create_mapping(swapper_pg_dir, _stext, (void *)VA2PA(_stext),
                   (uint64_t)(_srodata - _stext), PTE_R | PTE_X);
    create_mapping(swapper_pg_dir, _srodata, (void *)VA2PA(_srodata),
                   (uint64_t)(_sdata - _srodata), PTE_R);
    create_mapping(swapper_pg_dir, _sdata, (void *)VA2PA(_sdata),
                   (uint64_t)PA2VA(PHY_END) - (uint64_t)_sdata, PTE_R | PTE_W);
    satp_val = SATP_SV39 | (VA2PA(swapper_pg_dir) >> 12);
    csr_write(satp, satp_val);
    asm volatile("sfence.vma" ::: "memory");
}
