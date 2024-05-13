def dfs(graph, start, infected):
    
    infected[start] = True
    for i in graph[start]:
        if not infected[i]:
            dfs(graph, i, infected)

node = int(input())
net = int(input())

graph = [[] for i in range(node + 1)]
for i in range(net):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in graph:
    j.sort()

infected = [False] * (node + 1)

dfs(graph, 1, infected)

print(infected.count(True) - 1)