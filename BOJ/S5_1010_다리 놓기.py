n = int(input())

def fac(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def brid(left, right):
    return fac(right) // (fac(left)  * fac(right - left))

for __ in range(n):
    n, k = map(int, input().split())
    print(brid(n, k))