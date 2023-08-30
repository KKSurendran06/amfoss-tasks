def checkPrime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

N = int(input("Enter a number: "))

for i in range(2, N):
    if checkPrime(i):
        print(i)

