#include <stdio.h>
int main() {
	int v, a, b, i;
	scanf("%d %d %d", &a, &b, &v);
	i = (v - b - 1) / (a - b) + 1;
	printf("%d", i);
	return 0;
}