#include <stdio.h>
int main() {
	int num1, num2, i, j, sum = 0, min = 9999999;
	scanf_s("%d %d", &num1, &num2);
	for (i = num1; i <= num2; i++) {
		for (j = 2; j < i; j++) {
			if (i % j == 0) {
				break;
			}
		}
		if (j == i) {
			sum += i;
			if (min > i) {
				min = i;
			}
		}
	}
	if (sum == 0) printf("-1");
	else {
		printf("%d\n", sum);
		printf("%d", min);
	}
	return 0;
}