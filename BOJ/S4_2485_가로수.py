import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())

street = []
for __ in range(n):
    street.append(int(sys.stdin.readline().strip()))

distances = [street[i + 1] - street[i] for i in range(n - 1)]

g = distances[0]
for i in distances[1 : ]:
    g = gcd(g, i)

print((street[-1] - street[0]) // g - n + 1)