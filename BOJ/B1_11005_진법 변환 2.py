n, m = map(int, input().split())

rmn = []
answer = ""
while n > 0:
    rmn.append(n % m)
    n //= m


for i in rmn[::-1]:
    if i > 9:
        answer += chr(55 + i)
    else:
        answer += str(i)

print(answer)

# n, m = map(int, input().split())

# chrs = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# answer = ""
# while n > 0:
#     answer += chrs[n % m]
#     n //= m
# print(answer[::-1])

# 아래는  사람들이 많이 쓰는 모범답안인데 그래도 내 답이 좀 더 정감 간달까,,ㅎㅎ,,,
# while문 안에 for문 내용을 넣으면 좀 더 깔끔하게 쓸 수 있을 것 같긴 함.