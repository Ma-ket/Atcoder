#include<stdio.h>

void swap(int *a, int x, int y){
    int tmp = a[x];
    a[x] = a[y];
    a[y] = tmp;
    return;
}

void sort(int *a, int head, int tail){
    int min = a[head];
    for(int i = head; i < tail; i++){
        if(min > a[i]){
            min = a[i];
        }
    }
    for(int i = head; i < tail; i++){
        if(min == a[i]){
            swap(a, head, i);
        }
    }
    return;
}

int main(void){
    // 入力
    int n, k;
    scanf("%d%d", &n, &k);
    int a[n];
    for(int i = 0; i< n; i++){
        scanf("%d", &a[i]);
    }

    // aの中身を順にする
    for(int i = 0; i < n - 1; i++){
        sort(a, i, n);
    }

    // aの整理する
    int a_sort[n];
    int j = 0;
    a_sort[j++] = a[0];
    for(int i = 1; i < n; i++){
        if(a[i] != a[i - 1]){
            a_sort[j++] = a[i];
        }
    }
    int length = j;

    // // debug
    // for(int i = 0; i < n; i++){
    //     printf("%d ", a[i]);
    // }
    // printf("\n");
    // for(int i = 0; i < length; i++){
    //     printf("%d ", a_sort[i]);
    // }
    // printf("\n");

    int max = 0;
    for(int i = 0; i < length; i++){
        if(a_sort[i] == max){
            max++;
        }
    }
    if(max > k){
        printf("%d\n", k);
    } else {
        printf("%d\n", max);
    }

    return 0;
}
