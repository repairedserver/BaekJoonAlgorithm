#include <stdio.h>
#include <string.h>
int main() {
	char input_words[101]; / 문자열 배열
		int N;
	scanf("%d", &N);
	int count = N;
	for (int i = 0; i < N; i++)
	{
		char first = '0';
		int Alphabet[26] = { 0, };
		scanf("%s", input_words);
		for (int j = 0; input_words[j] != '\0'; j++) {
			if (first != input_words[j]) {
				first = input_words[j];
				Alphabet[input_words[j] - 'a'] += 1;
			}
			if (Alphabet[input_words[j] - 'a'] == 2) {
				count -= 1;
				break;
			}
		}
	}
	printf("%d", count);
	return 0;
}