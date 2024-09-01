#include <stdio.h>

// void debug(int *p, int len) {
//     for (int i = 0; i < len; i++) {   // debug
//         printf("%d-", p[i]);        // debug
//     }                               // debug
//     printf("\n");                   // debug
// }

int main(){
    int n;
    scanf("%d", &n);
    int h[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &h[i]);
    }

    int *p = h;
    long long t = 0;
    while (h[n - 1] > 0) {
        int num = 0;
        if (*p >= 5) {
            num = *p / 5;
            *p = *p % 5;
            t += num * 3;
        } else if (++t % 3 == 0) {
            *p -= 3;
        } else {
            *p -= 1;
        }
        if (*p <= 0) {
            p++;
            // debug(h, n);  // debug
            // printf("%lld\n", t); // debug
        }
    }
    printf("%lld\n", t);

    return 0;
}
