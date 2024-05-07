from collections import deque

N, K = map(int, input().split())

queue = deque()
answer = []

for i in range(N):
    queue.append(i+1)

for i in range(N):
    for j in range(K-1):
        item = queue.popleft()
        queue.append(item)
    answer.append(queue.popleft())

print(str(answer).replace('[','<').replace(']','>'))
