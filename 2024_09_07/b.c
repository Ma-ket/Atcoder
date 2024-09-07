#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int i,j,k;
    int a[n][n];
    for (i = 0; i < n; i++) {
        for (int j = 0; j < i + 1; j++) {
            scanf("%d", &a[i][j]);
        }
    }

    int pre_sts = 1;
    for (k = 1; k <= n; k++) {
        // printf("pre: %d\n", pre_sts);               // debug
        if (pre_sts >= k) {
            pre_sts = a[pre_sts-1][k-1];
        } else {
            pre_sts = a[k-1][pre_sts-1];
        }
    }
    printf("%d\n", pre_sts);

    return 0;
}
