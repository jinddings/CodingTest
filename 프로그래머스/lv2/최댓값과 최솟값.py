def solution(s):
    answer = ''
    arr = [int(i) for i in list(map(int,s.split()))]
    answer += str(min(arr)) +' '+ str(max(arr))
    return answer