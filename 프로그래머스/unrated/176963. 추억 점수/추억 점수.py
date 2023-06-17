def solution(name, yearning, photo):
    answer = []    
    name_yearning_dict = dict()
    for i in range(len(name)):
        name_yearning_dict[name[i]] = yearning[i]
    
    for persons in photo:
        score = 0
        for person in persons:
            score += name_yearning_dict.get(person,0)
        
        answer.append(score)

    return answer
