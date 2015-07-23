#include <stdio.h>

int solution(void);

int main(void) {
    printf("%d\n", solution());
    return 0;
}

int solution(void) {
    int n;
    int sum = 0;

    for (n = 0; n < 1000; n++) {
        if (n % 3 == 0 || n % 5 == 0) {
            sum += n;
        }
    }

    return sum;
}
