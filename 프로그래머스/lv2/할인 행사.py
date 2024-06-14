from collections import Counter

memo = {}

def isPossible(discount, day):
    discount_arr = discount[day:day + 10]
    counter = Counter(discount_arr)
    if memo == counter:
        return True
    else:
        return False


def solution(want, number, discount):
    answer = 0
    for w, n in zip(want, number):
        memo[w] = n

    for i in range(0, len(discount) - 9):
        if isPossible(discount, i):
            answer += 1

    return answer