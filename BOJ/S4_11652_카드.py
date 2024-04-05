import sys

n = int(sys.stdin.readline())

dic = {}

for _ in range(n):
    i = int(sys.stdin.readline())
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

lst = list(dic.keys())

lst.sort(key = lambda x : [-dic[x], x])

print(lst[0])

# 람다 쓰면 카운터 콜렉션 부럽지 않음. 요소가 가장 많은, 혹은 가장 적은 수 뽑을 때 이 문제를 떠올릴 것.