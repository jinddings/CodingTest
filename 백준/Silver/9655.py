memo = {1 : True, 2: False, 3: True, 4: False}
def solution(n):
    if n <= 0:
        return

    if n not in memo:
        memo[n] = not solution(n-1) or not solution(n-3)

    return memo[n]


N = int(input())


print("SK") if solution(N) else print("CY")