
visited = {}
data = []

n,m = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

graph = []
for i in range(n):
    graph.append(list(map(int,input())))


def dfs(graph, x,y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if graph[x][y] == 0 :
        graph[x][y] = 1
        for i in range(4):
            dfs(graph,x+dx[i],y+dy[i])
        return True
    return False


count =0
for i in range(n):
    for j in range(m):
        if dfs(graph,i,j) == True:
            count += 1


print(count)

