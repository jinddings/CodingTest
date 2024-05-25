memo = {0:1, 1:1}

def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = factorial(n-1) * n

    return memo[n]

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    print(factorial(M) // (factorial(M-N) * factorial(N)))



