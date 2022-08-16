#include <stdio.h>
int main() {
	char input[101];
	while (fgets(input, 101, stdin))
		printf("%s", input);
	return 0;
}

// scanf 함수는 ' '(space), '\t'(tab), '\n'(enter) 모두 구분자로 사용
//fgets 함수는 '\n'(enter)만을 구분자로 사용