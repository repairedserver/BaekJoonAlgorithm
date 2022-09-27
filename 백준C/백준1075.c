#include<stdio.h>
int main() {
    int n, f, temp, i;
    scanf("%d %d", &n, &f);
    n = (n / 100) * 100;
    for (i = 0; i < 100; i++) {
        temp = n;
        if ((temp += i) % f == 0)
            break;
    }
    if (i < 10) printf("0");
    printf("%d", i);
}