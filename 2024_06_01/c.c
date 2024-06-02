#include <stdio.h>

int main(void) {
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    int key[m][n];
    char r[m];
    for (int i = 0; i < m; i++) {
        int c;
        scanf("%d", &c);
        for (int j = 0; j < c; j++) {
            int a;
            scanf("%d", &a);
            key[i][a - 1] = 1;
        }
        scanf("%s", &r[i]);
    }
    int res = 0;
    for (int i = 0; i < (1 << n); i++) {
        int tf[n];
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                tf[j] = 1;
            } else {
                tf[j] = 0;
            }
        }
        int jud = 1;
        for (int j = 0; j < m; j++) {
            int ck = 0;
            for (int p = 0; p < n; p++) {
                if (key[j][p] == 1 && tf[p] == 1) {
                    ck++;
                }
            }
            if (ck >= k && r[j] == 'x') {
                jud = 0;
            }
            if (ck < k && r[j] == 'o') {
                jud = 0;
            }
        }
        if (jud == 1) {
            res++;
        }
    }
    printf("%d\n", res);
    return 0;
}
