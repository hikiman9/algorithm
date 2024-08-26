s = input()

partial = set(list())

for i in range(len(s)):
    for j in range(0, len(s)):
        partial.add(s[j:j + i + 1])

print(len(partial))