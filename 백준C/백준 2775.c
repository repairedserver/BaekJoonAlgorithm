#include <stdio.h>
int main(){
  int arr[15][15] = {0,};
  int test,h,w;
  for(int i=0; i<15; i++){
    arr[0][i] = i;
  }
  for(int i=1; i<15; i++){
    for(int j=1; j<15; j++){
      arr[i][j] = arr[i-1][j] + arr[i][j-1];
    }
  }
  scanf("%d",&test); 
  for(int i=0;i<test;i++){
    scanf("%d %d", &h, &w);  
    printf("%d\n", arr[h][w]);  
  }
	return 0; 
}
