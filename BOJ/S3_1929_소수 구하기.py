def isPrime(a):
    if a == 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

n, m = map(int, input().split())

for i in range(n, m + 1):
    if isPrime(i):
        print(i)