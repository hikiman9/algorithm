import sys

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

n = int(input())
for __ in range(n):
    k = int(sys.stdin.readline().strip())
    if k <= 1:
        k = 2
    while True:
        if isPrime(k):
            print(k)
            break
        k += 1
        