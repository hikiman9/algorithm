n = int(input())
nList = list(map(int, input().split()))

m = int(input())
mList = list(map(int, input().split()))

sg = {}
for i in nList:
    if i not in sg:
        sg[i] = 1
    else:
        sg[i] += 1

for i in mList:
    if i in sg:
        print(sg[i], end=" ")
    else:
        print(0, end=" ")