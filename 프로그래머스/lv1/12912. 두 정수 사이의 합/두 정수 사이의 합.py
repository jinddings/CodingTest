def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return a,b

def solution(a, b):
    
    
    answer = 0
    if b < a :
        a,b = swap(a,b)
    for i in range(a,b+1):
        answer += i
    return answer