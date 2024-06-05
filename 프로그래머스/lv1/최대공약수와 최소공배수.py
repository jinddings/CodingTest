def solution(n, m):
    answer = []
    G = 1
    L = min(n, m)

    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            G = i

    for i in range(min(n, m), n * m + 1):
        if i % n == 0 and i % m == 0:
            L = i
            break

    answer.append(G)
    answer.append(L)
    return answer