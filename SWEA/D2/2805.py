T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]

    mid = (N-1)//2

    result = 0
    cnt = 0
    for col in range(N):
        for row in range(cnt+1):
            if row == 0 :
                result += farm[mid][col]
            else :
                result += farm[mid+row][col]
                result += farm[mid-row][col]

        if col < mid :
            cnt+=1
        else:
            cnt-=1

    print("#{} {}".format(test_case,result))
