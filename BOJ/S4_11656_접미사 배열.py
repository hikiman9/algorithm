word = input()

suffix = [word[i:] for i in range(len(word))]

suffix.sort()

for i in suffix:
    print(i)