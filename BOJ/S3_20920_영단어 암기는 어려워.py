import sys

n, k = map(int, input().split())

counter = {}
vocab = []

for __ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) < k:
        continue
    if word not in counter:
        counter[word] = 1
        vocab.append(word)
    else:
        counter[word] += 1

vocab.sort(key = lambda x: [-counter[x], -len(x), x])

print(vocab)