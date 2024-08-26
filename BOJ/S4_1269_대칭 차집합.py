n, m = map(int, input().split())
setA = set(list(map(int, input().split())))
setB = set(list(map(int, input().split())))

set1 = setA - setB
set2 = setB - setA

print(len(set1) + len(set2))