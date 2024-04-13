def dfs(graph, cur_v):
    visited[cur_v] = True
    print(cur_v,end=' ')
    for next_v in graph[cur_v]:
        if next_v not in visited:
            dfs(graph,next_v)

visited = {}
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

dfs(g,1)