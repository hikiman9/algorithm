import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if farm[x][y] == 1:
        farm[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False

tc = int(input())

for i in range(tc):
    m, n, k = map(int, input().split())
    farm = [[0] * n for __ in range(m)]
    for j in range(k):
        a, b = map(int, input().split())
        farm[a][b] = 1
    count = 0
    for k in range(m):
        for l in range(n):
            if dfs(k, l):
                count += 1
    print(count)


# import sys
# sys.setrecursionlimit(10000)

# 이 코드는 재귀의 한도를 풀어주는 함수이다.
# 만약 재귀를 사용해서 풀어야 하는 문제라면, 해당 코드는 선택이 아닌 필수이다.
# 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다. 
# 따라서 재귀로 문제를 풀 경우 드물지 않게 이 제한에 걸리게 되는데, 
# 문제는 코딩테스트 환경에서는 에러메세지를 볼 수 없다는 것이다. 
# 함정에 빠지지 않기 위해 재귀함수를 사용한다면 잊지말고 꼭 써주어야 한다.

# 라고 함,,,,