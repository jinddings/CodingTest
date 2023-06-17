def solution(phone_number):
    answer = ''
    fourNums = phone_number[-4:]
    
    for i in range(len(phone_number)-4):
        answer = answer + '*'
    
    answer = answer + fourNums
    return answer