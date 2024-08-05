n = int(input())
arr = list(map(int, input().split()))

# dp 배열 초기화 및 첫 번째 값 설정
dp = [0] * n
dp[0] = arr[0]

# dp를 사용한 최대 연속합 계산
for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

# dp 배열 중 가장 큰 값을 출력
print(max(dp))