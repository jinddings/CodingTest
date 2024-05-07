from collections import deque

N = int(input())

queue = deque()
for i in range(1,N+1): queue.append(i)

while len(queue) > 1 :
    queue.popleft()
    item = queue.popleft()
    queue.append(item)

print(queue.popleft())
