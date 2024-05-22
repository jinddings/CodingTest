memo = {0:0, 1:1, 2:1}
def fibo(n):
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

input_n = int(input())

print(fibo(input_n))