#include <stdio.h>

int main() {
    char s[101];
    char *sp;
    scanf("%s", s);
    sp = s;

    if (0x41 <= *sp && *sp <= 0x5a) {
        sp++;
        while (*sp != '\0') {
            if (0x61 <= *sp && *sp <= 0x7a) {
                sp++;
            } else {
                printf("No\n");
                return 0;
            }
        }
        printf("Yes\n");
    } else {
        printf("No\n");
    }

  return 0;
}
