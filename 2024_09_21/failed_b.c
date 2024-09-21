#include <stdio.h>
#include <math.h>

#define POWER(d) ((int)pow(3, d))

int main() {
    int m = 59048;
    // scanf("%d", &m);


    int a[20];
    int n = 0;
    for (int i = 1; i <= 20; i++) {
        int digits = 0;
        for (int j = 5; j > 0; j--) {
            if (m / (int)pow(10, j) != 0) {
                digits = j + 1;
                break;
            }
        }

        digits = digits * 2;
        if (m >= POWER(digits)) {
            m -= POWER(digits);
        } else if (m >= POWER(--digits)) {
            m -= POWER(digits);
        } else {
            m -= POWER(--digits);
        }
        a[i - 1] = digits;
        printf("%d %d,\n", m, digits);
        if (m <= 0) {
            n = i;
            break;
        }
    }

    printf("%d\n", n);
    for (int i = 0; i < n; i++) {
        if (i == n - 1) {
            printf("%d\n", a[i]);
        } else {
            printf("%d ", a[i]);
        }
    }

    return 0;
}
