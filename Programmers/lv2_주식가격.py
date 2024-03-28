def solution(prices):

    answer = []

    for i in range(len(prices)):
        answer.append(i)
    
    answer = answer[::-1]

    stack = []

    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    
    return answer