while True:
    brackets = []
    strs = input()
    if strs == ".":
        break

    is_balanced = True

    for i in strs:
        if i == "(" or i == "[":
            brackets.append(i)
        elif i == ")":
            if brackets and brackets[-1] == "(":
                brackets.pop()
            else:
                is_balanced = False
                break
        elif i == "]":
            if brackets and brackets[-1] == "[":
                brackets.pop()
            else:
                is_balanced = False
                break

    if is_balanced and not brackets:
        print("yes")
    else:
        print("no")
