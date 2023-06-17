def solution(arr):
    answer = arr
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] :
            arr[i] = -1
    
    answer = [i for i in arr if i != -1]
    return answer