for test_case in range(1, 11):
    T = int(input())
    N = 100
    graph = [input() for _ in range(N)]

    longest = 0

    for k in range(2, N + 1):
        for i in range(N):
            for j in range(N):
                if j + k > N:
                    break
                else:
                    str_row = str(graph[i][j:j + k])
                    str_row_rev = str_row[::-1]
                    if str_row == str_row_rev:
                        if len(str_row) > longest: longest = len(str_row)

                col_str = ""
                for t in range(k):
                    if j + k > N:
                        break
                    col_str = col_str + str(graph[j + t][i])

                str_col = str(col_str)
                str_col_rev = str_col[::-1]
                if str_col == str_col_rev:
                    if len(str_col) > longest: longest = len(str_col)

    print("#{} {}".format(T, longest))
