from collections import deque

N = int(input())
result = [[0]*N for _ in range(N)]
graph = [list(map(int,input().split())) for _ in range(N)]

def bfs(graph, start_v):
    visited = {}
    queue = deque()
    queue.append(start_v)

    while queue:
        cur_v = queue.popleft()
        for next_v in range(N):
            if (next_v not in visited) and graph[cur_v][next_v] == 1:
                queue.append(next_v)
                visited[next_v] = True
                result[start_v][next_v] =1


for i in range(N):
    bfs(graph,i)

for row in result:
    print(*row)




