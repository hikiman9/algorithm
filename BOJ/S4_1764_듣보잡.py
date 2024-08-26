n, m = map(int, input().split())

nevheard = {}
for __ in range(n):
    nevheard[input()] = 0

answer = []

for __ in range(m):
    nevseen = input()
    if nevseen in nevheard:
        answer.append(nevseen)

answer.sort()
print(len(answer))
for i in answer:
    print(i)