# def solution(s):
#     answer = ''
#     arr = s.split()
#     for word in arr:
#         for i in range(len(word)):
#             if i % 2 == 0:
#                 answer += word[i].upper()
#             else :
#                 answer += word[i].lower()
#         answer += ' '
#     return answer[0:-1]


def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]