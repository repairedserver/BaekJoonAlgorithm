#include <stdio.h> 
int main() {
    int a, b, c, d = -1;
    int result, input, count = 0;

    scanf("%d", &input);
    result = input;

    while (d != result) {
        a = input / 10;
        b = input % 10;
        c = (a + b) % 10;
        d = (b * 10) + c;
        input = d;
        count++;
    }
    printf("%d", count);
    return 0;
}