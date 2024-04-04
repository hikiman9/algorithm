import sys

n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    lst.append(list(sys.stdin.readline().split()))


lst.sort(key = lambda x : int(x[0]))

for i in lst:
    print(i[0], i[1])