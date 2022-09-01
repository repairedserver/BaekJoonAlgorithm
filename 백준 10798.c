#include <stdio.h>
int main() {
	int i, j;
  char str_read[5][15];
	for(i=0; i<5; i++) {
		scanf("%s", str_read[i]);
	}
	for(j=0; j<15; j++) {
		for(i=0; i<5; i++) {
			if(str_read[i][j] == NULL)
				continue;
			else
				printf("%c", str_read[i][j]);
		}
	}
	printf("\n");
	return 0;
}
