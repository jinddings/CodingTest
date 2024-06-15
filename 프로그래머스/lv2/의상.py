def solution(clothes):
    answer = 1
    dict_clothes = {}
    for v, k in clothes:
        if k not in dict_clothes:
            dict_clothes[k] = []
        dict_clothes[k].append(v)

    for key in dict_clothes:
        answer *= len(dict_clothes[key]) + 1

    return answer - 1