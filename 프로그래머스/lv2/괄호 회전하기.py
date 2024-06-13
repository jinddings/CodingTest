def isCorrect(s):
    stack = []
    for item in s:
        if item == '(' or item == '{' or item == '[':
            stack.append(item)
        else:
            if not stack:
                return False
            elif item == ')' and stack[-1] == '(':
                stack.pop()
            elif item == ']' and stack[-1] == '[':
                stack.pop()
            elif item == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

    return False if stack else True

def solution(s):
    answer = 0

    for i in range(len(s)):
        s = "".join(s[1:] + s[:1])
        if isCorrect(s):
            answer += 1

    return answer