import sys

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
n = int(input())
for __ in range(n):
    k = int(sys.stdin.readline().strip())
    while True:
        if isPrime(k):
            print(k)
            break
        k += 1