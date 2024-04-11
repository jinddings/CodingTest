
def solution(N):
    remain_cost = N
    coin_nums = 0
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        coin_nums += remain_cost // coin
        remain_cost %= coin

    return coin_nums


print(solution(1260))
ㅉ