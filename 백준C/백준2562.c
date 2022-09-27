#include <stdio.h>
int main() {
	int input;
	int max = 0;
	int pos = 0;
	for (int i = 1; i < 10; ++i) {
		scanf("%d", &input);
		if (input > max) {
			max = input;
			pos = i;
		}
	}
	printf("%d\n%d\n", max, pos);
	return 0;
}