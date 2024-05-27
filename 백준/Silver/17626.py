import sys
memo = {0:0,1:1}
def solution(n):
    for i in range(2, n+1):
        min_num = i
        j = 1
        while j**2<=i:
            min_num = min(min_num, memo[i-j**2])
            j+=1

        memo[i] = min_num +1


    return memo[n]


N = int(input())

print(solution(N))



