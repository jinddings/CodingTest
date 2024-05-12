
N = int(input())

def dfs(cur_v):
    for next_v in graph[cur_v]:
        if next_v not in visited:
            visited[next_v] = cur_v
            dfs(next_v)


visited = {1 : 0}
graph = {}

for i in range(1,N+1):
    graph[i] = []

for _ in range(1,N):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2,N+1):
    print(visited[i])