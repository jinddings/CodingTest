def solution(d, budget):
    answer = 0
    d.sort()
    print(d)
    cost = 0
    for i in range(len(d)):
        if(cost+d[i]>budget):
            break
        else:
            cost += d[i]
            answer +=1
        
        
    return answer