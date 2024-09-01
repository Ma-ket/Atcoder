#include <stdio.h>

int ab(int a) {
    if (a > 0) {
        return a;
    }
    return a * (-1);
}

int main() {
    int n;
    scanf("%d", &n);
    int a[n];
    char s[n + 1];
    for (int i = 0; i < n; i++) {
        scanf("%d %c", &a[i], &s[i]);
    }

    int tired = 0;
    int bef_L = -1;
    int bef_R = -1;
    for (int i = 0; i < n; i++){
        if (s[i] == 'L') {
            if (bef_L >= 0) {
                tired += ab(a[i] - bef_L);
            }
            bef_L = a[i];
        } else {
            if (bef_R >= 0) {
                tired += ab(a[i] - bef_R);
            }
            bef_R = a[i];
        }
    }
    printf("%d\n", tired);

    return 0;
}
