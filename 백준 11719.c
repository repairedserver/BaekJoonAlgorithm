#include <stdio.h>
int main() {
	char input[101];
	while (fgets(input, 101, stdin))
		printf("%s", input);
	return 0;
}

// scanf �Լ��� ' '(space), '\t'(tab), '\n'(enter) ��� �����ڷ� ���
//fgets �Լ��� '\n'(enter)���� �����ڷ� ���