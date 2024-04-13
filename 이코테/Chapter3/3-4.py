def solution(n,k):
    global count
    if n == 2 or n//k == 1:
        count +=1
        return
    elif n%k == 0 :
        count +=1
        solution(n//k,k)
    else :
        count +=1
        solution(n-1,k)


n,k = map(int, input().split())
count = 0
solution(n,k)
print(count)


