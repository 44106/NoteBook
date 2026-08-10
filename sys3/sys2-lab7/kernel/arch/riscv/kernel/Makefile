ASM_SRC := $(wildcard *.S)
C_SRC   := $(wildcard *.c)

obj-y := $(ASM_SRC:.S=.o) $(C_SRC:.c=.o)
.PHONY: all clean
all: $(obj-y)
clean:
	rm -f *.o
%.o: %.S
	$(GCC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
%.o: %.c
	$(GCC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
