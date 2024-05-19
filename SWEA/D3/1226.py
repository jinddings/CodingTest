def isValid(r,c):
    if 0 <= r < row_len and 0<= c< col_len:
        return True
    return False
def dfs(r,c):
    global result
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    visited[r][c] = True
    for i in range(4):
        next_r = r+dr[i]
        next_c = c+dc[i]

        if isValid(next_r,next_c) :
            if maze[next_r][next_c] == 0:
                if not visited[next_r][next_c]:
                    dfs(next_r,next_c)
            elif maze[next_r][next_c] == 3:
                result = 1
                return


for test_case in range(1,11):
    T = int(input())
    maze = [list(map(int,input()))for _ in range(16)]
    row_len = len(maze)
    col_len = len(maze[0])
    visited = [[False] * col_len for _ in range(row_len)]
    result = 0

    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    for i in range(row_len):
        for j in range(col_len):
            if maze[i][j] == 2:
                start_x = i
                start_y = j
            elif maze[i][j] == 3:
                end_x = i
                end_y = j

    dfs(start_x,start_y)

    print("#{} {}".format(T,result))