#include <stdio.h>
int main() {
    int coin[] = { 500,100,50,10,5,1 }; //엔
    int money, i = 0, cnt = 0;
    scanf("%d", &money);

    money = 1000 - money;
    while (money != 0) { //동전이 거스름돈보다 큼
        if (coin[i] > money) {
            i++;
            continue;
        }
        else {
            money -= coin[i];
            cnt++;
        }
    }
    printf("%d\n", cnt);
    return 0;
}
