from collections import deque

N = int(input())
queue = deque()
for i in range(1, N + 1): queue.append(i)
stack = [0]
arr = []


def solution():
    global N, stack, arr
    for i in range(N):
        num = int(input())
        if stack[-1] < num:
            while stack[-1] < num:
                stack.append(queue.popleft())
                arr.append("+")

        if stack[-1] == num:
            stack.pop()
            arr.append("-")
        else:
            print("NO")
            return False

    return True


if solution():
    for str in arr:
        print(str)
