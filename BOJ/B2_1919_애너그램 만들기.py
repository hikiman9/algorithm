import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

aic = []
bic = []
for _ in range(26):
    aic.append(0)
    bic.append(0)

for i in range(26):
    aic[i] = a.count(chr(i + 97))
    bic[i] = b.count(chr(i + 97))

answer = 0
for i in range(26):
    answer += abs(aic[i] - bic[i])

print(answer)