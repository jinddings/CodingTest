def solution(s):
    str_arr = list(s)
    stack = []

    for i in str_arr:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0