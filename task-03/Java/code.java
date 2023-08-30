import java.util.Scanner;

public class Main {
    public static boolean checkPrime(int n) {
        if (n < 2) {
            return false;
        }

        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int N = scanner.nextInt();

        for (int i = 2; i <= N; i++) {
            if (checkPrime(i)) {
                System.out.print(i + " ");
            }
        }
        
        scanner.close(); // Close the scanner
    }
}

