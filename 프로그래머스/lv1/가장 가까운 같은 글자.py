memo = {}

def solution(s):
    answer = [-1]
    memo[s[0]] = 0
    for i in range(1, len(s)):
        if s[i] in memo:
            answer.append(i - memo[s[i]])
        else:
            answer.append(-1)
        memo[s[i]] = i

    return answer