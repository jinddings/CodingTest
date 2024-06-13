def solution(k, tangerine):
    answer = 0
    memo = {}
    for i in tangerine:
        if i not in memo:
            memo[i] = 1
        else:
            memo[i] += 1

    memo = dict(sorted(memo.items(), key=lambda x: x[1], reverse=True))
    for i in memo:
        if k <= 0:
            return answer
        k -= memo[i]
        answer += 1

    return answer