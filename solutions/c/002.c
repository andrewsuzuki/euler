#include <stdio.h>

int solution(void);

int main(void) {
    printf("%d\n", solution());
    return 0;
}

int solution(void) {
    int nl, n, new_n;
    int sum = 0;

    for (nl = 1, n = 2; n < 4e6; nl = n, n = new_n) {
        if (n % 2 == 0) {
            sum += n;
        }
        new_n = n + nl;
    }

    return sum;
}
