k = int(input())

sheet = []
for __ in range(k):
    n = int(input())
    if n == 0:
        sheet.pop()
    else:
        sheet.append(n)

print(sum(sheet))