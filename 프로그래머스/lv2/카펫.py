def solution(brown, yellow):
    answer = []
    x = 1
    y = 1
    for i in range(yellow, 0, -1):
        if yellow % i == 0:
            x = i
            y = yellow // i

        if 2 * x + 2 * y + 4 == brown:
            answer.append(x + 2)
            answer.append(y + 2)
            break
    return answer