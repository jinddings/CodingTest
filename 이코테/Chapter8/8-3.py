x = int(input())

dp = {0:0, 1:0}
for i in range(2, x+1):
    # a
    dp[i] = dp[i-1] + 1
    # b
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # c
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    # d
    elif i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])