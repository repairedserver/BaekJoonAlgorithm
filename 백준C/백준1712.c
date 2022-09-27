#include <stdio.h>
int main() {
	int m, n, s = 0, min = 1000;
	scanf("%d %d", &m, &n);

	for (int i = 1; i * i <= n; i++) {
		s += i * i;
		if (i * i < min) {
			min = i * i;
		}
	}
	printf("%d\n%d", s, min);
	return 0;
}