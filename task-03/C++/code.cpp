 #include <iostream>

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

using namespace std;

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;

    for (int i = 2; i <= n; i++) {
        if (checkprime(i)) {
            cout << i << " ";
        }
    }
    
    cout << "\n" ;
    return 0;
}