def jacad(str1, str2):
    inter = 0
    union = 0
    if len(str2) > len(str1):
        str1, str2 = str2, str1

    if len(str1) == 0 and len(str2) == 0:
        return 1

    # intersection
    for ch in set(str1 + str2):
        inter += min(str1.count(ch), str2.count(ch))
    # union
    for ch in set(str1 + str2):
        union += max(str1.count(ch), str2.count(ch))

    return inter / union


def strToList(str_):
    result = []
    for i in range(len(str_) - 1):
        tmp = str_[i:i + 2]
        for ch in tmp:
            if ord(ch) > ord('z') or ord(ch) < ord('a'):
                break
        else:
            result.append(tmp)

    return result


def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    str1_list = strToList(str1)
    str2_list = strToList(str2)

    answer = jacad(str1_list, str2_list)
    return int(answer * 65536)