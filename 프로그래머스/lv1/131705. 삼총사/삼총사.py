from itertools import combinations

def solution(number):
    answer = 0
    combinationList = list(combinations(number,3))
    print(combinationList)
    
    for comb in combinationList:
        if (comb[0] + comb[1] + comb[2]) == 0 :
            answer += 1
    return answer