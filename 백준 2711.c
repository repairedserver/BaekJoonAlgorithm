#include<stdio.h>
#include<string.h>
int main() {
	int T, i,j,index;
	char str[81];
	scanf("%d",&T);
	for (i = 0; i < T; i++) {
		scanf("%d %s", &index, str);
		for (j = 0; j < strlen(str); j++) {
			if (j != index-1)
			printf("%c", str[j]);
		}
		printf("\n");
	}
  return 0;
}
