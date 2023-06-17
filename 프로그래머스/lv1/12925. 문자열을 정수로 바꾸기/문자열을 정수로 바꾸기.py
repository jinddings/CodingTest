def solution(s):
    answer = 0
    
    if s[0] == '-':
        answer = round(float(s))
    elif s[0] == '+':
        answer = round(float(s))
    else:
        answer = float(s)
        
    return answer