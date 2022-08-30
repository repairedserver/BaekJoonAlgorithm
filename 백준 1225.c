#include<stdio.h>
#include<string.h>
int main() {
    long long int n = 0;
    char a[10001], b[10001];
    scanf("%s %s", a, b);
    for (int i = 0; i < strlen(a); i++) {
        for (int j = 0; j < strlen(b); j++) {
            n += (a[i] - '0') * (b[j] - '0');
        }
    }
    printf("%lld", n);
    return 0;
}
