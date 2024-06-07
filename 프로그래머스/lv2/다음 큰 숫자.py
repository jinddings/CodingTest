def solution(n):
    answer = 0
    bin_n = str(bin(n))[2:]
    bigger_n = n

    while True:
        bigger_n += 1
        bin_bigger_n = str(bin(bigger_n))[2:]

        if bin_n.count('1') == bin_bigger_n.count("1"):
            answer = bigger_n
            break

    return answer