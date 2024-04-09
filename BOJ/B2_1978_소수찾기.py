def isPrime(a):
    if a == 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))

print(sum([int(isPrime(i)) for i in nums]))