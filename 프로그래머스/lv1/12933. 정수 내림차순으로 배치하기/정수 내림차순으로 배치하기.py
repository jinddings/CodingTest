def solution(n):
    answer = 0
    
    num_list = []
    while n!=0:
        num_list.append(n % 10)
        n//=10
    
    number = ""
    num_list.sort(reverse = True)
    for num in num_list :
        number += str(num)
    
    answer = int(number)
    return answer