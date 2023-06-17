def solution(s):
    answer = True
    
    countP = s.count('p') + s.count('P')
    countY = s.count('y') + s.count('Y')
    
    if countP == countY and countP == 0 and countY == 0:
        return True
    elif countP == countY and countP != 0 and countY != 0:
        return True
    else :
        return False
