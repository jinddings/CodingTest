dp = {1:1, 2:2, 3:4}
def solution(N):
    for i in range(4,N+1):
        dp[i] = dp[i-1] + dp[i-2]+ dp[i-3]

    return dp[N]


T = int(input())
for test_case in range(T):
    N = int(input())
    print(solution(N))


