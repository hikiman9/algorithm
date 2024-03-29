import sys

word = sys.stdin.readline().strip()



for i in range(97, 123):
    print(word.count(chr(i)), end = " ")
