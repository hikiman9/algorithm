import sys
sys.setrecursionlimit(1000000)

def dfs(graph, start, visited):
    visited[start] = True
    answer.append([start, len(answer) + 1])
    # print(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m, r = map(int, input().split())

graph = [[] for __ in range(n + 1)]
for __ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph: 
    i.sort(reverse=True)

visited = [False] * (n + 1)

answer = []
dfs(graph, r, visited)
for i in range(1, len(visited)):
    if not visited[i]:
        answer.append([i, 0])
answer.sort(key=lambda x : x[0])

for i in answer:
    print(i[1])