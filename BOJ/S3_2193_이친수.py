# a = []
# for i in range(32, 64):
#     a.append(bin(i)[2:])

# print(a)

# count = 0

# for i in a:
#     if "11" not in i and i.startswith("1"):
#         count += 1

# print(count)

# 걍 피보나치 수열 문제임 대충 5~6항까지 위에 코드로 돌려보면 답 나옴.
# DP는 일단 알아보고 초기 항들 구해보는 게 맞나 싶음

n = int(input())

d = [0, 1, 1]

for _ in range(n):
    d.append(d[-1] + d[-2])

print(d[n])