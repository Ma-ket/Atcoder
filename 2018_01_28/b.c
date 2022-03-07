#include <stdio.h>
#include <math.h>

int main(){
    int money;
    int coin5;
    int coin500;

    scanf("%d", &money);

    coin500 = money / 500;
    coin5 = (money-500*coin500)/5;

    printf("%d\n", coin500*1000 + coin5*5);

    return 0;
}
