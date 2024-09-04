import sys

def soe(n):
    
    primes = [True] * (n * 2 + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n * 2:
        if primes[p]:
            for i in range(p * p, n * 2 + 1, p):
                primes[i] = False
        p += 1
    
    return sum([1 for i in range(n + 1, n * 2 + 1) if primes[i]])
    




while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(soe(n))