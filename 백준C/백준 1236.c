#include<stdio.h>
int main(){
	char arr[50][50] = { 0,};
	int R;
	int C;
	scanf("%d %d", &R, &C);
	for (int i = 0; i < R; i++){
		scanf("%s", arr[i]);
	}
	int tempR = R;
	int tempC = C;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if (arr[i][j] == 'X')
			{
				tempR--;
				break;
			}
		}
	}
	for (int i = 0; i < C; i++)
	{
		for (int j = 0; j < R; j++)
		{
			if (arr[j][i] == 'X')
			{
				tempC--;
				break;
			}
		}
	}
	if (R == 1){
		printf("%d\n", tempC);
	}
	else if (C == 1){
		printf("%d\n", tempR);
	}
	else{
		printf("%d\n", tempR < tempC ? tempC : tempR);
	}
	return 0;
}
