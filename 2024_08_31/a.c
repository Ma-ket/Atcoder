#include <stdio.h>

int main() {
    int a, b;
    scanf("%d%d", &a, &b);

    int x = a - b;

    if ((x = a - b) == 0) {
        printf("1\n");
    } else {
        if (x % 2 != 0) {
            printf("2\n");
        } else {
            printf("3\n");
        }
    }

    return 0;
}
