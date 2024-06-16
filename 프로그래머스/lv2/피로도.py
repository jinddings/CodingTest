from itertools import permutations

def solution(k, dungeons):
    cnt_dungeons = []
    for p_dungeons in permutations(dungeons, len(dungeons)):
        cnt = 0
        tmp = k
        for min_cost, consume_cost in p_dungeons:
            if tmp >= min_cost:
                tmp -= consume_cost
                cnt += 1
        cnt_dungeons.append(cnt)

    return max(cnt_dungeons)