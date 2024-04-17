n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

dp = {}
for i in range(m+1):
    dp[i] = 10001

dp[0] = 0

for i in range(n):
    for j in range(array[i], m + 1):
        if dp[j - array[i]] != 10001:
            dp[j] = min(dp[j], dp[j - array[i]]+1)

if dp[m] != 10001:
    print(dp[m])
else:
    print(-1)
