#include <stdio.h>
int main() {  
    int a[10] = { 0, };
    int n, tmp;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 10; j++) {
            scanf("%d", &a[j]);
        }
        for (int k = 0; k < 10; k++) {
            for (int x = 0; x < 9; x++) {
                if (a[x] < a[x + 1]) {
                    tmp = a[x];
                    a[x] = a[x + 1];
                    a[x + 1] = tmp;
                }
            }
        }
        printf("%d\n", a[2]);
    }
    return 0;
}
