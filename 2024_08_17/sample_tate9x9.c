#include <stdio.h>

int main() {
    int arr[10][10];
    int cnt = 0;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            arr[j][i] = cnt;
            cnt++;
        }
    }

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%2d ", arr[i][j]);
        }
        printf("\n");
    }

    return 0;
}
 /*
90 .. 10 0
91 .. 11 1
92 .. 12 2
93 .. 13 3
..........
97 .. 17 7
98 .. 18 8
99 .. 19 9
 */
