N = int(input())
array = list(map(int,input().split()))

dp = {0:array[0], 1: max(array[0],array[1])}


for i in range(2,N):
    dp[i] = max(array[i-1], array[i-2] + array[i])

print(dp[N-1])