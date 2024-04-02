n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][:j + 1])

print(sum(dp[n]) % 10007)

# 계단 수 풀고 보니까 굉장히 쉽게 풀었음
# dp[n][i]이 "n자리 수에서 정수 i가 마지막에 오는 경우의 수" 라고 생각하고 풂