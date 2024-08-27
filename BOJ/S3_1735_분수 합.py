a, b = map(int, input().split())
c, d = map(int, input().split())

def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

def lcm(n, m):
    return n * m // gcd(n, m)

k = lcm(b, d) 

numerator = (a * (k // b)) + (c * (k // d))

g = gcd(numerator, k)

print(numerator // g, k // g)