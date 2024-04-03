n = int(input())
lst = list(map(int, input().split()))

dp = [1] * n 

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# n = int(input())
# lst = list(map(int, input().split()))

# lens = []
# for i in range(len(lst) - 1):
#     cnt = 1
#     std = lst[i]
#     for j in range(i + 1, len(lst)):
#         if lst[j] > std:
#             cnt += 1
#             std = lst[j]
#     lens.append(cnt)

# print(max(lens))

# 문제 보고 얼마 안 있다가 생각해낸 답이다. 웬만한 테스트 케이스를 다 통과하길래
# 오늘도 저질러 버렸나,,,하고 제출했더니 바로 실패가 나옴.
# 본인 전용 디버거에게 예외케이스를 찾으라고 명령하니
# 5
# 10 50 20 30 40
# 와 같은 케이스를 가져왔다. 예외 케이스 보고 아예 접근 방식이 잘못된 걸 깨닫고 답 찾아봄

# 답안에서도 어김 없이 메모이제이션을 사용한 걸 보고는 양치기를 해야 좀 익숙해지겠구나
# DP를 점화식 노가다로 가볍게 볼 문제가 아니구나 꺠달았다
# 그리고 뭔가 사고의 반전이 필요하다고 느낀 게 쉬운 계단 수 문제에서도 그렇고
# 배열 혹은 문자열의 시작이 아니라 끝을 먼저 채워나가는 방식으로 푸는 경우가 잦은 것 같다.