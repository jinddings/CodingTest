import sys
input = sys.stdin.readline
from collections import deque

N,M,K,X = map(int,input().split())
distance = [[] for _ in range(N+1)]

def bfs(graph,start_v):
    queue = deque()
    visited = {start_v : True}
    distance[start_v] = 0
    queue.append(start_v)

    while queue :
        cur_v = queue.popleft()
        for next_v in graph[cur_v]:
            if next_v not in visited:
                queue.append(next_v)
                visited[next_v] = True
                distance[next_v] = distance[cur_v]+1

graph = {}
for i in range(1,N+1):
    graph[i] = []

for _ in range(M):
    start_v, end_v = map(int,input().split())
    graph[start_v].append(end_v)

bfs(graph,X)

result = []
for i in range(1,N+1):
    if distance[i] == K:
        result.append(i)

if len(result) != 0:
    for vertex in result:
        print(vertex)
else :
    print(-1)