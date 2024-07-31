import sys

n = int(input())

words = []
for __ in range(n):
    words.append(sys.stdin.readline().strip())

words = set(words)
words = list(words)

words.sort(key=lambda x:(len(x), x))

for i in words:
    print(i)