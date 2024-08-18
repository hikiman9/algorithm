from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

cands = []
for i in combinations(cards, 3):
    if sum(i) == m:
        print(sum(i))
        break
    if sum(i) < m:
        cands.append(sum(i))

else:
    print(max(cands))