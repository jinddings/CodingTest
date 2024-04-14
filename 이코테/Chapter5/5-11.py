from collections import deque

visited = {}
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(g,x,y):
    queue = deque()
    queue.append((x,y))
    count = 1

    while queue:
        cur_x,cur_y = queue.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx <0 or ny<0 or nx>=n or ny>=m :
                continue
            if g[nx][ny] == 0 :
                continue
            if g[nx][ny] == 1 :
                g[nx][ny] = g[cur_x][cur_y] + 1
                queue.append((nx,ny))

    return g[n-1][m-1]


n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

print(bfs(graph,0,0))




