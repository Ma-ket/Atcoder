#include<stdio.h>
int main(){
    int c;
    for(c=0; c<5000; c++){
        printf("echo %d | ./B\n", c);
    }
    return 0;
}