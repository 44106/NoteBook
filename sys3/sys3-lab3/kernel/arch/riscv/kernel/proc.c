#include <mm.h>
#include <printk.h>
#include <private_kdefs.h>
#include <proc.h>
#include <stdlib.h>

static struct task_struct *task[NR_TASKS];
static struct task_struct *idle;
struct task_struct *current;

void __dummy(void);
void __switch_to(struct task_struct *prev, struct task_struct *next);

void dummy_task(void) {
    uint64_t local = 0;
    uint64_t last_counter = 0;

    while (1) {
        if (current->counter == last_counter) {
            continue;
        }

        last_counter = current->counter;
        printk("[PID = %ld @ %#lx] Running. local = %ld\n",
               current->pid, (uint64_t)current, ++local);
    }
}

void task_init(void) {
    srand(2025);

    idle = (struct task_struct *)alloc_page();
    idle->state = TASK_RUNNING;
    idle->pid = 0;
    idle->priority = 0;
    idle->counter = 0;
    current = idle;
    task[0] = idle;

    for (int i = 1; i < NR_TASKS; ++i) {
        struct task_struct *p = (struct task_struct *)alloc_page();

        task[i] = p;
        p->state = TASK_RUNNING;
        p->pid = i;
        p->priority = rand() % (PRIORITY_MAX - PRIORITY_MIN + 1) + PRIORITY_MIN;
        p->counter = 0;
        p->thread.ra = (uint64_t)__dummy;
        p->thread.sp = (uint64_t)p + PGSIZE;
    }

    printk("...task_init done!\n");
    printk("2025 ZJU Computer System III\n");
}

void switch_to(struct task_struct *next) {
    struct task_struct *prev;

    if (current == next) {
        return;
    }

    printk("switch to [PID = %ld, PRIORITY = %ld, COUNTER = %ld]\n",
           next->pid, next->priority, next->counter);

    prev = current;
    current = next;
    __switch_to(prev, next);
}

void do_timer(void) {
    if (current == idle || current->counter == 0) {
        schedule();
        return;
    }

    current->counter--;
    if (current->counter == 0) {
        schedule();
    }
}

void schedule(void) {
    struct task_struct *next = NULL;
    long next_counter;

    while (1) {
        next_counter = -1;
        next = NULL;

        for (int i = 1; i < NR_TASKS; ++i) {
            if (task[i]->state != TASK_RUNNING) {
                continue;
            }
            if ((long)task[i]->counter <= next_counter) {
                continue;
            }

            next_counter = task[i]->counter;
            next = task[i];
        }

        if (next_counter > 0) {
            break;
        }

        for (int i = 1; i < NR_TASKS; ++i) {
            task[i]->counter = task[i]->priority;
            printk("SET [PID = %ld, PRIORITY = %ld, COUNTER = %ld]\n",
                   task[i]->pid, task[i]->priority, task[i]->counter);
        }
    }

    switch_to(next);
}
