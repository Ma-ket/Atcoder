#include <stdio.h>

int main() {
    double x;
    scanf("%lf", &x);

    int aaa = (int)(x * 1000.0);
    if (aaa % 10 != 0){
        printf("%.3lf\n", x);
    } else {
        aaa = aaa / 10;
        if (aaa % 10 != 0) {
            printf("%.2lf\n", x);
        } else {
            aaa = aaa / 10;
            if (aaa % 10 != 0) {
                printf("%.1lf\n", x);
            } else {
                printf("%d\n", aaa / 10);
            }
        }
    }
    return 0;
}
