from collections import deque

n = int(input())
balloons = deque(enumerate(map(int, input().split()), 1))  # (index, value) 형태로 저장

answer = []

while balloons:
    index, paper = balloons.popleft()
    answer.append(index)

    if balloons:
        if paper > 0:
            balloons.rotate(-(paper - 1))  # 풍선의 번호만큼 회전 (양수 방향)
        else:
            balloons.rotate(-paper)  # 풍선의 번호만큼 회전 (음수 방향)

print(' '.join(map(str, answer)))
