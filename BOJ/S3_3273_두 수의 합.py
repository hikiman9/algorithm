# 냅다 뺀 값 찾기로 했다가 시간 초과가 나옴
# 짱구 굴리다가 투포인터를 써보기로 함
# 배열 자체가 복잡한 게 아니라서 어렵진 않았던 것 같음

# --------------------------------------------------------------------

# import sys

# n = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))
# x = int(sys.stdin.readline())

# answer = 0

# for i in range(len(numbers) - 1):
#     if x - numbers[i] in numbers[i + 1:]:
#         answer += 1

# print(answer)

import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

numbers.sort()
left = 0
right = n - 1

answer = 0

while left < right:
    total = numbers[left] + numbers[right]
    if total > x:
        right -= 1
    elif total < x:
        left += 1
    else:
        answer += 1
        left += 1
        right -= 1

print(answer)