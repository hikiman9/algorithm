n = int(input())

dance = {}

for __ in range(n):
    a, b = input().split()
    if a not in dance:
        dance[a] = 0
    if b not in dance:
        dance[b] = 0
    if a == "ChongChong" or b == "ChongChong" or dance[a] == 1 or dance[b] == 1:
        dance[a] = 1
        dance[b] = 1

print(sum(dance.values()))