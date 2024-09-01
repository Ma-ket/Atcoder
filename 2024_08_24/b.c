#include <stdio.h>

void swap(int *pa, int *pb) {
    int tmp;
    tmp = *pa;
    *pa = *pb;
    *pb = tmp;
}

void sort(int *p, int len) {
    int i, j;
    for (i = 0; i < len; i++) {
        for (j = len - 1; j > i; j--) {
            if (p[j] > p[j - 1]) {
                int tmp;
                tmp = p[j];
                p[j] = p[j - 1];
                p[j - 1] = tmp;
            }
        }
    }
}

// void debug(int *p, int len) {
//     for (int i = 0; i < len; i++) {   // debug
//         printf("%d-", p[i]);        // debug
//     }                               // debug
//     printf("\n");                   // debug
// }

int main() {
    int n;
    scanf("%d", &n);
    int a[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    int cnt = 0;
    sort(a, n);
    do {
        a[0] -= 1;
        a[1] -= 1;
        sort(a, n);
        cnt++;
        // debug(a, n);
    } while (a[1] > 0);
    printf("%d\n", cnt);

    return 0;
}

/*
1233
3321 > 2221
2221 > 1121
2111 > 1011
1110 > 0010
*/
