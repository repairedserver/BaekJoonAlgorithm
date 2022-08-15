#include <stdio.h>
int main() {
	int gibon, suik, biyong;

	scanf("%d %d %d", &gibon, &suik, &biyong);
	
	if (suik >= biyong) printf("-1\n");
	else printf("%d\n", gibon / (biyong / suik) - 1);
	return 0;
}