#include <stdio.h>
int main() {
	char a;
	while (scanf("%c", &a) != -1) {
		printf("%c", a);
	}
	return 0;
}