#include <stdio.h>

int main() {
    int l, r;
    scanf("%d%d", &l, &r);

    if ((l == 1 && r == 1) || (l == 0 && r == 0)) {
        printf("Invalid\n");
    } else if (l == 1) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }

    return 0;
}
