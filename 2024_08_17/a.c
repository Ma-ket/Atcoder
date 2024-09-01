#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    if (b > c) {
        c += 24;
        a += 24;
    }

    if (b < a && a < c) {
        printf("No");
    } else {
        printf("Yes");
    }
    printf("\n");
    return 0;
}
