T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


for test_case in range(1, T + 1):
    N = int(input())
    priceList = list(map(int, input().split()))
    profit = 0

    idx = len(priceList) - 1

    while idx > 0 :
        for i in range (idx-1, -1, -1) :
            maxCost = priceList[idx]
            if maxCost < priceList[i]:
                idx = i
                break
            else :
                profit += maxCost - priceList[i]
        else :
            break
    print("#{0} {1}".format(test_case, profit))




