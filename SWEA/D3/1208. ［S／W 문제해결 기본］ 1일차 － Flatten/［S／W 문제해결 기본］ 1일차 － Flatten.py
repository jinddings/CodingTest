
def dump():
    maxIndex = data.index(max(data))
    minIndex = data.index(min(data))
    data[maxIndex] -= 1
    data[minIndex] += 1

T = 10
for test_case in range(1, T + 1):
    dumpCount = int(input())
    data = list(map(int, input().split()))

    for _ in range(dumpCount) :
        if max(data) - min(data) <= 1 :
            break
        dump()
    print("#{0} {1}".format(test_case,max(data)-min(data)))