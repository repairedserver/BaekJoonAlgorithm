#include <string.h>
#include <stdio.h>
int main() {
	char n[10];
	char tmp;
	scanf("%s", n);
	for (int i = 0; i < strlen(n) - 1; i++) {
		for (int j = 0; j < strlen(n); j++) {
			if (n[j] < n[j + 1]) {
				tmp = n[j];
				n[j] = n[j + 1];
				n[j + 1] = tmp;
			}
		}
	}
	printf("%s", n);
	return 0;
}
