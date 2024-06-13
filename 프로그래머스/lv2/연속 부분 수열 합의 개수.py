def solution(elements):
    memo = set()
    elements = elements * 2
    for i in range(len(elements) // 2):
        for j in range(len(elements) // 2):
            memo.add(sum(elements[j:j + i + 1]))

    return len(memo)