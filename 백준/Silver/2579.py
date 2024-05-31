
dp = {0:0}
def solution(n):

    if n < 3 :
        return sum(stairs)
    else:
        dp[1] = stairs[1]
        dp[2] = stairs[1] + stairs[2]

        for i in range(3,n+1):
            dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

        return dp[n]

N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))

print(solution(N))



