

def dfs(index,pTaste, pKcal):
    global maxTaste
    if pKcal > L:
        return
    if maxTaste < pTaste :
        maxTaste = pTaste
    if index == N :
        return

    taste, kcal = foods[index]
    dfs(index+1, pTaste,pKcal)
    dfs(index+1, pTaste + taste, pKcal + kcal )

T = int(input())
for test_case in range(1, T + 1):
    N,L = map(int,input().split())
    foods = [list(map(int,input().split())) for _ in range(N)]
    maxTaste = 0


    dfs(0,0,0)
    print("#{} {}".format(test_case,maxTaste))