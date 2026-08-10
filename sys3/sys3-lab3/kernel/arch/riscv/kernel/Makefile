ASM_SRC := $(wildcard *.S)
C_SRC   := $(wildcard *.c)

obj-y := $(ASM_SRC:.S=.o) $(C_SRC:.c=.o)
DEPS := $(ASM_SRC:.S=.d) $(C_SRC:.c=.d)
.PHONY: all clean
all: $(obj-y)
clean:
	rm -f *.o *.d
%.o: %.S
	$(GCC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
%.o: %.c
	$(GCC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

-include $(DEPS)
