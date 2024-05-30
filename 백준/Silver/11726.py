dp = {1:1, 2:2}

def solution(n):
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

N = int(input())
print(solution(N) % 10007)

