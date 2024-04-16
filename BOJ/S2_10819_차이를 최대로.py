# n = int(input())
# lst = list(map(int, input().split()))

# lst.sort()
# answer = []

# if n % 2 == 0:
#     i = 0
#     answer.append(lst[n // 2 - 1])
#     while i < n // 2 - 1:
#         answer.append(lst[n - 1 - i])
#         answer.append(lst[i])
#         i += 1
#     answer.append(lst[n // 2])

# else:
#     i = 0
#     answer.append(lst[n // 2])
#     while i < n // 2:
#         answer.append(lst[n - 1 - i])
#         answer.append(lst[i])
#         i += 1

# summ = 0
# for i in range(len(answer) - 1):
#     summ += abs(answer[i] - answer[i + 1])

# print(summ)

from itertools import permutations

n = int(input())
lst = list(map(int, input().split()))

permu = list(permutations(lst, n))

def absSum(arr):
    total = 0
    for i in range(len(arr) - 1):
        total += abs(arr[i] - arr[i + 1])
    return total

answer = []

for i in permu:
    answer.append(absSum(i))

print(max(answer))

# n의 범위가 3~8이라고 할 떄 그냥 바로 순열을 생각했으면 좋았으련만
# 겉멋만 들어서 앗 시간복잡도와 최적화를 위해 멋진 풀이 방법을 생각해야겠군
# 하고 쓴 코드는 진행률 94% 에서 오답나옴 ㅅㅂ