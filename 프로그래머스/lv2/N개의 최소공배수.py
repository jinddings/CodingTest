def gcd(a, b):
    p = a % b
    if p == 0:
        return b
    return gcd(b, p)


def solution(arr):
    answer = 1
    for item in arr:
        answer = (answer * item) // gcd(item, answer)

    return answer