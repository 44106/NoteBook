#include <mm.h>
#include <proc.h>
#include <stdlib.h>
#include <printk.h>
#include <stddef.h> 
#include <private_kdefs.h>

static struct task_struct *task[NR_TASKS]; // 线程数组，所有的线程都保存在此
static struct task_struct *idle;           // idle 线程
struct task_struct *current;               // 当前运行线程

void __dummy(void);
void __switch_to(struct task_struct *prev, struct task_struct *next);

// 在这里添加或实现这些函数：
// - void dummy_task(void);
// - void task_init(void);
// - void do_timer(void);
// - void schedule(void);
// - void switch_to(struct task_struct* next);
void dummy_task(void) {
    uint64_t local = 0;
    uint64_t prev_cnt = 0;
    while (1) {
        // 只有当时间片发生变化时才输出，避免刷屏
        if (current->counter != prev_cnt) {
            // 针对 priority=1 的特殊处理（Lab文档要求）
            if (current->counter == 1) {
                current->counter = 0;
            }
            prev_cnt = current->counter;
            printk("[PID = %ld] %ld\n", current->pid, ++local);
        }
    }
}
void task_init(void) {
    srand(2025);
    idle = (struct task_struct*)alloc_page();
    idle->state = TASK_RUNNING;
    idle->pid = 0;
    idle->priority = 0;
    idle->counter = 0;
    current = idle;
    task[0] = idle;
    for (int i = 1; i < NR_TASKS; i++) {
        struct task_struct* p = (struct task_struct*)alloc_page();
        task[i] = p;
        p->state = TASK_RUNNING;
        p->pid = i;
        p->priority = (rand() % (PRIORITY_MAX - PRIORITY_MIN + 1)) + PRIORITY_MIN;
        p->counter = 0;
        p->thread.ra = (uint64_t)__dummy;
        p->thread.sp = (uint64_t)p + PGSIZE;
    }
    printk("...task_init done!\n");
}
void switch_to(struct task_struct* next) {
    if (current == next) {
        return;
    }
    struct task_struct* prev = current;
    current = next;
    __switch_to(prev, next);
}
void do_timer(void) {
    if (current == idle || current->counter == 0) {
        schedule();
        return;
    }
    current->counter--;
    if (current->counter > 0) {
        return;
    }
    else {
        current->counter = 0; 
        schedule();
    }
}

void schedule(void) {
    struct task_struct* next = NULL;
    long max_c = -1;
    while (1) {
        max_c = -1; 
        next = NULL;
        for (int i = 0; i < NR_TASKS; i++) {
            if (task[i]->state == TASK_RUNNING) {
                if ((long)task[i]->counter > max_c) {
                    max_c = task[i]->counter;
                    next = task[i];
                }
            }
        }
        if (max_c > 0) {
            break;
        }
        for (int i = 0; i < NR_TASKS; i++) {
            task[i]->counter = task[i]->priority;
        }
    }
    switch_to(next);
}
