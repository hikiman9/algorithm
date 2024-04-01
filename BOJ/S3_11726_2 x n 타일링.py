n = int(input())

answers = [0, 1, 2, 3]

for i in range(n):
    answers.append(answers[-1] + answers[-2])

print(answers[n] % 10007)