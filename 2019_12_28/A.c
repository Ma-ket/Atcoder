#include <stdio.h>
#include <math.h>

int main(){
    int N, A, B;
    int x, y;

    scanf("%d %d %d", &N, &A, &B);
    if(N<2&&pow(10, 18)<N){
        return 0;
    }else if((A<1) && (A>=B && B>N)){
        return 0;
    }
    x=B-A;
    y=N-A;
    if(B-1<y){
        if(x%2==1){
            printf("%d\n", B-1);
        }else{
            printf("%d\n", x/2);
        }
    }else{
        if(x%2==1){
            printf("%d\n", y);
        }else{
            printf("%d\n", x/2);
        }
    }
    return 0;
}
/*
萎えた
問題文
2N人の卓球選手が、
1からN
までの番号がついたN台の卓で実戦練習を行います。

練習は複数のラウンドからなります。各ラウンドでは、選手たちは1卓につき1ペアの合計Nペアに分かれます。そして、各ペアの選手同士で試合を行い、1人が勝利してもう1人が敗北します。

卓Xで勝利した選手は、次のラウンドでは卓X−1で試合を行います。 ただし、卓1で勝利した選手は卓1に留まります。
同様に、卓Xで敗北した選手は、次のラウンドでは卓X+1で試合を行います。 ただし、卓Nで敗北した選手は卓Nに留まります。ある2人の選手は友達同士で、最初のラウンドの試合を異なる卓A,B
で行います。 彼らは十分な腕前を持ち、各試合での自分の勝敗を自由に操れるとします。 この2人同士で試合を行えるまでに、最小で何回のラウンドが必要でしょうか？

制約
2≤N≤10^18
1≤A<B≤N
入力中のすべての値は整数である。
*/
/*
答えは、
min(A-1, N-B)+1+(B-A-1)/2 である。
https://img.atcoder.jp/agc041/editorial.pdf
*/