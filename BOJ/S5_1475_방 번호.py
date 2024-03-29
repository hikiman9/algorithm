import sys

number = sys.stdin.readline().strip()

cnt = []

for i in range(10):
    cnt.append(number.count(str(i)))

a = max([cnt[0], cnt[1], cnt[2], cnt[3], cnt[4], cnt[5], cnt[7], cnt[8]])
if (cnt[6] + cnt[9]) // 2 == (cnt[6] + cnt[9]) / 2:
    b = (cnt[6] + cnt[9]) // 2
else:
    b = (cnt[6] + cnt[9]) // 2 + 1

print(max(a, b))
