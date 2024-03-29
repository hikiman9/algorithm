import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = sys.stdin.readline().strip().split()
    if sorted(list(a)) == sorted(list(b)):
        print("Possible")
    else:
        print("Impossible")