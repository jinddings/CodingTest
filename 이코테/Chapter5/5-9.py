from collections import deque


def bfs(graph,start_v):
    q = deque()
    q.append(start_v)
    visited = {start_v : True}

    while q :
        cur_v = q.popleft()
        print(cur_v, end=' ')
        for next_v in graph[cur_v]:
            if next_v not in visited:
                q.append(next_v)
                visited[next_v] = True


g = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

bfs(g,1)