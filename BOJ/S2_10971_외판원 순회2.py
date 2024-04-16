from itertools import permutations

n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

lst = [i for i in range(n)]

permu = list(permutations(lst, n))

def travSum(arr):
    total = 0
    for i in range(len(arr) - 1):
        total += cost[i][i + 1]
    total += cost[arr[-1]][arr[0]]
    return total

answer = []

for i in permu:
    answer.append(travSum(i))

print(min(answer))