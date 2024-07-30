n = int(input())
nList = list(map(int, input().split()))

m = int(input())
mList = list(map(int, input().split()))

a = {}
for i in nList:
    a[i] = 0

for i in mList:
    if i in a:
        print(1, end=" ")
    else:
        print(0, end=" ")