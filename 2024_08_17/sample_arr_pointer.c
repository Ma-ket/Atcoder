#include <stdio.h>

#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof(arr[0]))

int sum(int *array, int len) {
    int cnt = 0;
    for (int i = 0; i < len; i++) {
        cnt += array[i];
        printf("%d ", cnt);
    }
    printf("\n");
    return cnt;
}

int main() {
    int a[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    printf("%d, %d\n", a[0], (int)ARRAY_SIZE(a));
    printf("%d\n", sum(a, (int)ARRAY_SIZE(a)));
    return 0;
}

/*
*array <- a[0]
array = 0
*/
