#include <string.h>

void *memset(void *restrict dst, int c, size_t n) {
	char* p = (char*)dst;
	for (size_t i = 0; i < n; i++) {
		p[i] = (char)c;
	}return dst;
}

size_t strnlen(const char *restrict s, size_t maxlen) {
	size_t i = 0;
	while (i < maxlen && s[i] != '\0') {
		i++;
	}return i;
}
