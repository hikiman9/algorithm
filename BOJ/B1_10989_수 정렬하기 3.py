import sys

n = int(sys.stdin.readline())

l = [0] * 10001

for _ in range(n):
    l[int(sys.stdin.readline())] += 1

for i in range(len(l)):
    if l[i] != 0:
        for j in range(l[i]):
            print(i)

# import sys

# n = int(sys.stdin.readline())

# nums = [int(sys.stdin.readline()) for _ in range(n)]

# for i in sorted(nums):
#     print(i)

# 이딴 식으로 풀었다가 틀린 문제
# 그것도 시간 초과가 아닌 메모리 초과였다. 처음 보는 유형의 오류라 조금 당황했음.
# 시간 초과라면야 어떻게든 잘 해봤겠지만 메모리 초과에 대해선 대처해 본 적이 없어서 바로 답 봄
# 풀이는 쉬운데 다만 메모리에 관해서 이런 방법을 생각해 낼 수 있어야 한다는 걸 배움