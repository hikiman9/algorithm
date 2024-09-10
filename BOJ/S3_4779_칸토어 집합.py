import sys
sys.setrecursionlimit(1000000)

import sys

def kanto(dashes):
    length = len(dashes)
    if length == 1:  # 더 이상 쪼갤 수 없을 때
        return dashes
    left = kanto(dashes[0 : length // 3])
    mid = " " * (length // 3)  # 중간 부분을 공백으로
    right = kanto(dashes[length // 3 * 2 :])
    return left + mid + right

input_data = sys.stdin.read().splitlines()

for line in input_data:
    n = int(line)
    if n == 0:
        print("-")  # n이 0일 때는 길이 1의 대시
    else:
        dashes = "-" * (3 ** n)  # 길이 3^n의 대시 문자열 생성
        print(kanto(dashes))
