def solution(s):
    answer = ''
    str_list = list(s)
    str_list.sort(reverse = True)
    
    for alpha in str_list:
        answer += alpha
    return answer