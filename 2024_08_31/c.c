#include <stdio.h>

long long f(long long a) {
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
    // 差の配列を作成
    int d[n - 1];
    for (int l = 0; l < n - 1; l++) {
        d[l] = a[l] - a[l + 1];
    }

    long long cnt_f = 0;
    for (i = 1; i < n - 1; i++) {
        if (a[i - 1] - a[i] != a[i] - a[i + 1]) {
            cnt += f(i - cnt_f);
            cnt_f = (long long)i;
        }
    }
    // cnt_f=1 なら0が帰ってくる
    cnt += f(n - 1 - cnt_f);

    printf("%lld\n", cnt);

    return 0;
}
