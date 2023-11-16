
T = int(input())
studentCount = 1000
for test_case in range(1, T + 1):
    test_case_num = int(input())
    scores = list(map(int,input().split()))
    dictScores = {}

    for i in range(len(scores) -1):
        score = scores[i]
        if scores[i] in dictScores :
            dictScores[score] += 1
        else :
            dictScores[score] = 1

    maxScore = max(dictScores, key = dictScores.get)

    print("#{0} {1}".format(test_case,maxScore))
