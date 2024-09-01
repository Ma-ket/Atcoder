#include <stdio.h>

int main() {
    int a = 1000000000;
    int n = 200000;
    printf("%d\n", n);
    for (int i = 0; i < n; i++) {
        printf("%d ", a);
    }
    printf("\n");
    return 0;
}
