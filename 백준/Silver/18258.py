import sys
input = sys.stdin.readline
from collections import deque

queue = deque()

N = int(input())

for i in range(N):
    arr = list(map(str,input().split()))

    if arr[0] == 'push':
        queue.append(int(arr[1]))
    elif arr[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif arr[0] == 'size':
        print(len(queue))
    elif arr[0] == 'empty':
        if not queue:
            print(1)
        else :
            print(0)
    elif arr[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif arr[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])