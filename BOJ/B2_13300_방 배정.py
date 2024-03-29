import sys

n, k = map(int, sys.stdin.readline().split())

boys = [0, 0, 0, 0, 0, 0]
girls = [0, 0, 0, 0, 0, 0]

for _ in range(n):
    s, grade = map(int, sys.stdin.readline().split())
    if s == 0:
        boys[grade - 1] += 1
    else:
        girls[grade - 1] += 1

answer = 0

for i in range(6):
    if girls[i] // k == girls[i] / k:
        answer += girls[i] // k
    else:
        answer += (girls[i] // k) + 1
    if boys[i] // k == boys[i] / k:
        answer += boys[i] // k
    else:
        answer += (boys[i] // k) + 1

print(answer)