#include <stdio.h>
int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	int abc = a * b * c;
	int arr[10] = { 0, };
	while (abc > 0) {
		++arr[abc % 10];
		abc /= 10;
	}
	for (int i = 0; i < 10; ++i) {
		printf("%d\n", arr[i]);
	}
	return 0;
}