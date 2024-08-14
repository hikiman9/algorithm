m = int(input())
n = int(input())

def isPrime(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

primes = []

for i in range(m, n + 1):
    if isPrime(i):
        primes.append(i)

if primes: 
    print(sum(primes))
    print(primes[0])
else: 
    print(-1)