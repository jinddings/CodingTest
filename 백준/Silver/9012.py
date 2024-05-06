import sys
input = sys.stdin.readline

def solution(str):
    stack = []
    for c in str:
        if c == "(":
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            stack.pop()

    if not stack:
        return True
    else :
        return False


N = int(input())
for i in range(N):
    if solution(input()):
        print("YES")
    else :
        print("NO")

