import sys
input = sys.stdin.readline
N,K = map(int,input().split())

graph = [[0]*N for _ in range(N)]

for _ in range(K):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

S = int(input())

for _ in range(S):
    a,b = map(int, input().split())
    if graph[a-1][b-1] :
        print(-1)
    elif graph[b-1][a-1]:
        print(1)
    else:
        print(0)
