# x = int(input())
# answer = 0
# while x > 1:
#     if x % 3 == 0:
#         x //= 3
#     elif (x - 1) % 3 == 0:
#         x -= 1
#     elif x % 2 == 0:
#         x //= 2
#     else:
#         x -= 1
#     answer += 1
#     print(answer)
#     print(x)

# 문제 내용 보고 개 쉬운 문젠데 이게 왜 실버,,,??라고 하며 달려 들었는데 개같이 실패
# 점화식이랑 관련된 문제이려나,,, 피보나치 수열이 쓰이나,,, 고민했지만 번뜩임 없이 답 찾아봄,,,

n = int(input())

answers = [0] * (n + 1)

for i in range(2, n + 1):
    answers[i] = answers[i - 1] + 1
    if n % 2 == 0:
        answers[i] = min(answers[i], answers[i // 2] + 1)
    if n % 3 == 0:
        answers[i] = min(answers[i], answers[i // 3] + 1)

print(answers[n])

# DP 구형 방법은
# 1. 작은 문제로 나눈다.
# 2. 작은 문제를 풀어 정답을 구한다. 
# 3. 작은 문제의 정답을 저장한다.
# 4. 큰 문제를 작은 문제로 나누어 1~3 단계를 반복한다.
# 인데 3단계의 '작은 문제의 정답을 저장한다.'를 메모제이션이라고 한다고 한다.
# 메모리 공간 비용을 사용함으로써 시간 비용을 줄이는,,,
# 문제 풀이 자체에 대한 이견이나 짚고 넘어가야 할 점은 크게 보이지 않는 것 같다.
# 그냥 다음에 비슷한 문제 나오면 잘 갖다 써야겠다는 느낌,,