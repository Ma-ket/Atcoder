#include <stdio.h>

long long f(int a) {
    // 階差数列の和
    return a * (a - 1) / 2;
}

int main() {
    int n;
    scanf("%d", &n);
    int a[n];
    int i;
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    long long cnt = n + (n - 1);
    int cnt_f = 0;
    for (i = 1; i < n - 1; i++) {
        if (a[i - 1] - a[i] != a[i] - a[i + 1]) {
            cnt += f(i - cnt_f);
            cnt_f = i;
        }
    }
    // cnt_f=1 なら0が帰ってくる
    cnt += f(n - 1 - cnt_f);

    printf("%lld\n", cnt);

    return 0;
}

