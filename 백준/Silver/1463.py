memo = {0:0, 1:0}
def solution(n):
    for i in range(2,n+1):
        min_ = memo[i-1] + 1
        if i % 3 == 0:
            min_ = min(memo[i//3] + 1, min_)
        if i % 2 == 0:
            min_ = min(memo[i//2] +1, min_)

        memo[i] = min_

    return memo[n]


N = int(input())
print(solution(N))