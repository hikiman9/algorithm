import sys

n = int(input())

numbers = []
counter = {}

for __ in range(n):
    k = int(sys.stdin.readline())
    if k not in counter:
        counter[k] = 1
    else:
        counter[k] += 1
    numbers.append(k)

numbers.sort()

max_freq = max(counter.values())
modes = [key for key, value in counter.items() if value == max_freq]
modes.sort()
if len(modes) > 1:
    mode_result = modes[1]
else:
    mode_result = modes[0]


print(round(sum(numbers) / len(numbers)))
print(numbers[len(numbers) // 2])
print(mode_result)
print(max(numbers) - min(numbers))