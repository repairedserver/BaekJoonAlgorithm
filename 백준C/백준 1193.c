#include <stdio.h>
int main() {
	int input;
	scanf("%d", &input);
	int k = 1;
	while (1) //∂Û¿Œ
	{
		if ((k - 1) * (k) / 2 < input && input <= (k) * (k + 1) / 2)
		{
			break;
		}
		k++;
	}

	if (k % 2 != 0)
	{
		int a = k * (k + 1) / 2;
		printf("%d", a - input + 1);
		printf("/");
		printf("%d", k - (a - input));
	}
	else
	{
		int a = k * (k + 1) / 2;
		printf("%d", k - (a - input));
		printf("/");
		printf("%d", a - input + 1);
	}
	return 0;
}