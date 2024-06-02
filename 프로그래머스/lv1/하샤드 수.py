def solution(x):
    sum_digit = sum(int(i) for i in str(x))
    return True if x%sum_digit == 0 else False