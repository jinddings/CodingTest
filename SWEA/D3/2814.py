T = int(input())
def dfs(cur_v,depth):
    global result
    if depth > result : result = depth
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            visited[next_v] = True
            dfs(next_v,depth+1)
            visited[next_v] = False


for test_case in range(1,T+1):
    N, M = map(int,input().split())
    graph = {}
    result = 0

    for i in range(1,N+1):
        graph[i] = []

    for i in range(M):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,N+1):
        visited = [False for _ in range(N+1)]
        visited[i] = True
        dfs(i,1)


    print("#{} {}".format(test_case,result))
