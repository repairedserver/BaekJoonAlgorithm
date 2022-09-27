#include <stdio.h>
int main(){
    int arr[8];
    int as = 0, des = 0;
    for(int i = 0; i < 8; i++)
        scanf("%d", &arr[i]);
    for(int i = 0; i < 4; i++){
        if(arr[i] == i+1 && arr[i] + arr[7 - i] == 9)
            as++;
        else if(arr[7-i] ==  i+1 && arr[i] + arr[7-i] == 9)
            des++;
    }
    if(as == 4)
        printf("ascending");
    else if(des == 4)
        printf("descending");
    else
        printf("mixed");
    return 0;
}
