T = int(input())


def sumList(matrix):
    tmp = 0
    for row in matrix:
        tmp += sum(row)
    return tmp


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = list()
    for i in range(N):
        board.append(list(map(int, input().split())))
    maxSum = 0

    maxKill = 0
    smallBoards = list()
    for row in range(N - M+ 1):
        for col in range(N - M+1):
            smallBoards = [row[col:col + M] for row in board[row:row + M]]
            sumVal = sumList(smallBoards)
            if maxSum < sumVal:
                maxSum = sumVal
            smallBoards = list()

    print("#{0} {1}".format(test_case,maxSum))