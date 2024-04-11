
def solution(N,M,K):
    answer = 0
    count = 0
    global data
    for i in range(M):
        if count < K :
            count += 1
            answer += data[-1]
        else :
            answer += data[-2]
            count = 0
    return answer


n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()


answer = solution(n,m,k)
print(answer)