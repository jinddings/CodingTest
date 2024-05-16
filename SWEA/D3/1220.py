T=10
for test_case in range(1,T+1):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        flag = 0
        for j in range(N):
            if table[j][i] == 1:
                flag = 1
            elif table[j][i] == 2:
                if flag:
                    result+=1
                    flag=0

    print("#{} {}".format(test_case,result))