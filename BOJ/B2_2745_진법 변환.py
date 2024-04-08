a, n = input().split()
n = int(n)

ords = []
for i in a:
    if i.isalpha():
        ords.append(ord(i) - 55)
    else:
        ords.append(int(i))
ords = ords[::-1]

answer = 0
for i in range(len(ords)):
    answer += (n ** i) * ords[i]
print(answer)