#include <stdio.h>
#include <string.h>
int main() {
    char a[1000000];
    int num = 0;
    scanf("%[^\n]s", a);

    if (a[0] != ' ') num++;

    for (int i = 1; i < strlen(a); i++)
        if (a[i - 1] == ' ' && a[i] != ' ') num++;

    printf("%d", num);

    return 0;
}