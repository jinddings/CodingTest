

for test_case in range(1,10+1):
    T = int(input())
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]

    sums = []

    for i in range(N):
        temp = 0
        for j in range(N):
            temp += arr[i][j]
        sums.append(temp)

    for j in range(N):
        tmp = 0
        for i in range(N):
            tmp += arr[i][j]
        sums.append(tmp)
    tmp = 0
    for i in range(N):
        tmp  += arr[i][i]

    sums.append(tmp)

    tmp = 0
    for i in range(N-1,-1,-1):
        tmp += arr[i][i]
    sums.append(tmp)

    print("#{} {}".format(test_case,max(sums)))

