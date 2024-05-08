import sys
input = sys.stdin.readline
from collections import deque

queue = deque()
N = int(input())

for i in range(N):
    command = list(map(str,input().split()))

    if command[0] == 'push_front':
        queue.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        queue.append((int(command[1])))
    elif command[0] == 'pop_front':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'pop_back':
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else :
            print(0)
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
