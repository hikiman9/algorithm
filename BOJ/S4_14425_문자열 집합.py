n, m = map(int, input().split())

s = []
for __ in range(n):
    s.append(input())

answer = 0
for __ in range(m):
    if input() in s:
        answer += 1

print(answer)