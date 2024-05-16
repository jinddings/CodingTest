T = int(input())

def check_sudoku():
    for i in range(9):
        dict_row = {}
        dict_col = {}
        for j in range(9):
            row = sudoku[i][j]
            col = sudoku[j][i]

            dict_squre = {}
            if row in dict_row:
                return False
            else:
                dict_row[row] = True
            if col in dict_col:
                return False
            else:
                dict_col[col] = True

            for a in range(3):
                for b in range(3):
                    num = sudoku[(i//3)*3 +a][(i//3)*3+b]

                    if num in dict_squre:
                        return False

                    else :
                        dict_squre[num] = True
    return True

for test_case in range(1,T+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)]

    print("#{} {}".format(test_case, 1 if check_sudoku() else 0))