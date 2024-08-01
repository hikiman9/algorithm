n, k = map(int, input().split())
ppl = [i + 1 for i in range(n)]

answer = []
comp = [0] * n

i = 0
while True:
    count = 0
    while count < k:
        if ppl[i % n] != 0:
            count += 1
        i += 1
    answer.append(ppl[(i - 1) % n])
    ppl[(i - 1) % n] = 0
    if ppl == comp:
        break

print("<", ", ".join(map(str, answer)), ">", sep="")