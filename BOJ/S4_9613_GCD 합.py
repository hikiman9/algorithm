import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(sys.stdin.readline())

for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    lst = lst[1:]
    temp = []
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            temp.append(gcd(lst[i], lst[j]))
    print(sum(temp))