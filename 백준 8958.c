#include <stdio.h>
#include <string.h>
int main() {
	int num, score = 0, score1 = 1;
	char ox[80];
	scanf("%d", &num);
	for (int i = 0; i < num; i++) {
		score = 0;
		score1 = 1;
		scanf("%s", ox);
		for (int j = 0; j < strlen(ox); j++) {
			if (ox[j] == 'O') {
				score += score1;
				score1++;
			}
			else if (ox[j] == 'X') {
				score1 = 1;
			}
		}
		printf("%d\n", score);
	}
	return 0;
}