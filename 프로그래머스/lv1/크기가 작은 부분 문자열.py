def solution(t, p):
    answer = 0
    arr = []
    for i in range(len(t) - len(p) + 1):
        arr.append(t[i:i + len(p)])

    for item in arr:
        if int(p) >= int(item):
            answer += 1
    return answer

