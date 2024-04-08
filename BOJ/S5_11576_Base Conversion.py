a, b = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))
num = num[::-1]

ten = 0
for i in range(len(num)):
    ten += (a ** i) * num[i]

answer = []

while ten > 0:
    answer.append(ten % b)
    ten //= b

print(*answer[::-1])