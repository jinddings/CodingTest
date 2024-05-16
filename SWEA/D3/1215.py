T = 10
N = 8
for test_case in range(1, T + 1):
    K = int(input())
    graph = [list(input()) for _ in range(N)]

    count = 0
    for i in range(N):
        for j in range(N-K+1):
            str_row = graph[i][j:j + K]
            str_row_reverse = str_row[::-1]
            if str(str_row) == str(str_row_reverse):
                count += 1

    for j in range(N):
        for i in range(N - K+1):
            str_col = []
            for k in range(K):
                str_col.append(graph[i+k][j])
            str_col_reverse = str_col[::-1]
            if str(str_col) == str(str_col_reverse):
                count += 1

    print("#{} {}".format(test_case, count))