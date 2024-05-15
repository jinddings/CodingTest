T = int(input())

for test_case in range(1, T + 1):
    N,K = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if grid[i][j] == 1:
                count += 1
            if grid[i][j] == 0 or j == N-1:
                if count == K :
                    result +=1
                count = 0

        for j in range(N):
            if grid[j][i] == 1:
                count += 1
            if grid[j][i] == 0 or j == N-1:
                if count == K:
                    result +=1
                count = 0


    print("#{} {}".format(test_case,result))



