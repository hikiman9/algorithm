n, k = map(int, input().split())

items = []
for _ in range(n):
    weight, value = map(int, input().split())
    items.append((weight, value))

dp = [0] * (k + 1)

for weight, value in items:
    for i in range(k, weight - 1, -1):  # 역순으로 진행
        dp[i] = max(dp[i], dp[i - weight] + value)
        print(dp)

