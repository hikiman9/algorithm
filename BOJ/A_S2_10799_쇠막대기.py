brck = input()

answer = 0

stk = []
for i in range(len(brck)):
    if brck[i] == "(":
        stk.append("(")
    else:
        if brck[i - 1] == "(":
            stk.pop()
            answer += len(stk)
        else:
            answer += 1
            stk.pop()

print(answer)

# 풀이가 생각보다 쉬움
# 막대기 잘랐을 떄 개수 늘어나는 걸 복잡하게 생각할 필요가 없었는 듯.
# ()를 다른 문자로 바꾸고 풀면 시간 초과가 뜰까 궁금함(안 뜸)