#include <stdio.h>
int reverse(int num) {
    int reverse = 0;
    while (num != 0) {
        reverse = reverse * 10 + num % 10;
        num /= 10;
    }
    return reverse;
}
int main() {
    int num;
    scanf("%d", &num);
    while (num) {
        int temp = reverse(num);
        if (temp == num) printf("yes\n");
        else printf("no\n");
        scanf("%d", &num);
    }
    return 0;
}
