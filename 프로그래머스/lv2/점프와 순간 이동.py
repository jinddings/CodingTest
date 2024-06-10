def suit(n, batt):
    if n == 1:
        return batt + 1
    if n % 2 == 0:
        return suit(n // 2, batt)
    else:
        return suit(n - 1, batt + 1)

def solution(n):
    ans = suit(n, 0)
    return ans