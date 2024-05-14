
visited = []

def adj(x):
    for i in range(x):
        if row[x] == row[i] or x-i == abs(row[x]-row[i]):
            return False
    return True


def dfs(start_v):
    global result
    if start_v == N :
        result += 1
    else:
        for i in range(N):
            row[start_v] = i
            if adj(start_v):
                dfs(start_v+1)

T = int(input())
for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    row = [0] * N
    dfs(0)
    print('#{} {}'.format(test_case,result))