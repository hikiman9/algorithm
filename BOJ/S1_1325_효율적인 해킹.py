import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

graph = [[] for __ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

def dfs(area, start, checked):
    global count
    checked[start] = True
    count += 1

    for i in area[start]:
        if checked[i] == False:
            dfs(area, i, checked)

hackable = [0]

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    count = 0
    dfs(graph, i, visited)
    hackable.append(count)

answer = []
king = max(hackable)

for i in range(len(hackable)):
    if hackable[i] == king:
        print(i, end = " ")