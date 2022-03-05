#include <stdio.h>
#include <string.h>

int main(){
    char S[6];

    scanf("%s", S);

    if(strlen(S)>6 || strlen(S)<1){
        return 0;
    }

    if(S[2]==S[3] && S[4]==S[5]){
        printf("Yes\n");
    }else{
        printf("No\n");
    }
    return 0;
}