#include <stdio.h>
#include <stdbool.h>

bool checkprime(int N) {
    if (N < 2) { 
        return false;
    }

    for (int i = 2; i * i <= N; i++) {
        if (N % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    printf("Enter a number n: ");
    scanf("%d", &n);

    for (int i = 2; i <= n; i++) {
        if (checkprime(i)) {
            printf("%d ", i);
        }
    } 
    printf("\n");
    return 0;
}
