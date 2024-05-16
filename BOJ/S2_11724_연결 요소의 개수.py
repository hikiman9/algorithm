import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for __ in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(graph, start, visited):
    
    global temp
    visited[start] = True
    temp.append(start)

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (n + 1)

answer = []

for i in range(1, n + 1):
    temp = []
    dfs(graph, i, visited)
    temp.sort()

    if temp not in answer:
        answer.append(temp)
    visited = [False] * (n + 1)

print(len(answer))