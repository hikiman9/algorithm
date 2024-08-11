import sys

def gdc(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gdc(a, b)

n = int(sys.stdin.readline())

for _ in range(n):
    i, j = map(int, sys.stdin.readline().split())
    print(lcm(i, j)) 