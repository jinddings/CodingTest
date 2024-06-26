def solution(n, words):
    memo = {words[0]: True}

    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1]:
            return [i % n + 1, i // n + 1]

        if words[i] not in memo:
            memo[words[i]] = True
        else:
            return [i % n + 1, i // n + 1]

    return [0, 0]