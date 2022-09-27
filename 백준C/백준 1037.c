#include <stdio.h>
int main() {
	int N, temp;
	scanf("%d", &N);
	int arr[50];
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (arr[i] < arr[j]) {
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}
	printf("%d", arr[0] * arr[N - 1]);
	return 0;
}