n, k = map(int, input().split())

def fac(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(fac(n) // (fac(n - k) * fac(k)))