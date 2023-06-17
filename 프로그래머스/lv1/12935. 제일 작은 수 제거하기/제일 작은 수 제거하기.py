def solution(arr):
    answer = []
    idx_min = arr.index(min(arr))
    arr.pop(idx_min)
    answer = arr
    
    if len(answer) == 0 :
        answer.append(-1)
        
    return answer