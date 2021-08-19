#include <stdio.h>
int main(){
    int N;
    scanf("%d", &N);
    if(N<0 || N>5000) return 0;
    int X;
    int i=0;
    int Sample;
    while(i<=N){
        X=i;
        Sample=i*1.08;
        if(N==Sample) break;
        i++;
    }
    if(N==X){
        printf(":(\n");
    }else{
        printf("%d\n", X);
    }
    return 0;
}