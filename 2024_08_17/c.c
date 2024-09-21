#include <stdio.h>
#include <math.h>

int sum(int *array, int len) {
    int cnt = 0;
    for (int i = 0; i < len; i++) {
        cnt += array[i];
    }
    return cnt;
}

int max_row(int *arr, int len) {
    int result = 1;
    for (int i = 0; i < len; i++) {
        result *= arr[i];
    }
    return result;
}

int main(){
    int n, k;
    scanf("%d%d", &n, &k);
    int r[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &r[i]);
    }

    int mx_rw = max_row(r, n);
    int array[mx_rw][n]
    for (int i = 0; i < mx_rw; i++) {
        for (int j = n - 1; j >= 0; j--) {  // 数列を作成
            array[i][j] = r[j];
            if (j == n - 1) {
                if (r[j] > 1) {
                    r[j]--;
                }
            } else if (r[j + 1] <= 1) {

            }
        }
        /*
        2 1 3
        2 1 2
        2 1 1
        */

        for(int j = 1; j <= r[i]; j++) {
            for (int l = 0; l < n; l++) {
                array[i][l] = j;
            }
        }

        for (int j = 0; j < n; j++) {
            for (int l = 1; l <= n; l++) {
                line[l - 1] = l;
            }
            if (sum(line, n) % k != 0) continue;
            if (r >= fusion(line, n)) {
                for (int l = 0; l < n; l++) {
                    printf("%d ", line[l]);
                }
                printf("\n");
            }
        }
    }

    return 0;
}
