import sys

n, m = map(int, input().split())

poke_idx = {}
poke_name = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    poke_idx[name] = i + 1
    poke_name[i + 1] = name

for __ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(poke_name[int(q)])
    else:
        print(poke_idx[q])