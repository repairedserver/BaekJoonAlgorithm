#include<stdio.h>
int main()
{
	int n;
	scanf("%d", &n);
	long long ans = 5;
	long long num = 7;
	for (int i = 2; i <= n; i++)
	{
		ans += num;
		num += 3;
		ans = ans % 45678;
	}
	printf("%lld", ans);
	return 0;
}