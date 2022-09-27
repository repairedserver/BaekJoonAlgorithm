#include<stdio.h>
#include<string.h>
int main() {
	int N;
	char a[51][51];
	int len;
	bool check = true;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%s", a[i]);
	}
	len = strlen(a[0]);
	if (N == 1) {
		printf("%s", a[0]);
	}
	else {
		for (int i = 0; i < len; i++) {
			check = true;
			for (int j = 0; j < N; j++) {
				if (a[j][i] != a[0][i]) check = false;
			}
			if (check == false) {
				a[0][i] = '?';
			}
		}
			printf("%s", a[0]);
	}
    return 0;
}
