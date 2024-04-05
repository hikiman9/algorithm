import sys

n, k = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

print(sorted(lst)[k - 1])