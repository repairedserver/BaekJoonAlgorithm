#include<stdio.h>
int main() {
    int num, tmp, i;
    int last = 0;
    int cur = 1;
    scanf("%d", &num);
    if (num < 2) {
        if (num == 0) printf("0");
        else printf("1");
    }
    else {
        for (i = 0; i < num - 1; i++) {
            tmp = cur + last;
            last = cur;
            cur = tmp;
        }
        printf("%d", tmp);
    }
    return 0;
}