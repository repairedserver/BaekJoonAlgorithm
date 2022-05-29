#include <stdio.h>
int main() {
	int nan[9]; //난쟁이들
	int total = 0; // 난쟁이 키 총합
	int over = 0; // 초과값
	int real_nan[7]; // 진짜 난쟁이들
	int orm; //오름차순 정렬
	int i, j;
	int p = 0, q = 0;

	for (i = 0; i < 9; i++) { // 난쟁이들 키 입력
		scanf_s("%d", &nan[i]);
		total += nan[i];
	}

	over = total - 100; //초과값

	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++) {
			if (nan[i] + nan[j] == over) {
				p = i;
				q = j;
				break;
			}
		}
	}

	j = 0;

	for (i = 0; i < 9; i++) {
		if (i != p && i != q) {
			real_nan[j] = nan[i];
			j++;
		}
	}

	for (i = 0; i < 7; i++) {
		for (j = i + 1; j < 7; j++)
			if (real_nan[i] > real_nan[j]) {
				orm = real_nan[i];
				real_nan[i] = real_nan[j];
				real_nan[j] = orm;
			}
	}
	for (i = 0; i < 7; i++) {
		printf("%d\n", real_nan[i]);
	}
	return 0;
}