import sys
from collections import deque

def bfs(graph, v, visited):
    
    que = deque([v])
    visited[v] = True

    while que:
        r = que.popleft()
        print(r, end=" ")
        for i in graph[r]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


def dfs(graph, v, visited):
    visited[v] = True

    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (n + 1)
dfs(graph, v, visited)
print("\n", end="")
visited = [False] * (n + 1)
bfs(graph, v, visited)