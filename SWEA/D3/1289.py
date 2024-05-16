
T = int(input())

def change_bit(start, value):
    global err_bit
    for i in range(start,len(answer_bit)):
        err_bit[i] = value

for test_case in range(1,T+1):
    answer_bit = list(map(int,input()))
    err_bit = [0 for _ in range(len(answer_bit))]

    count = 0
    for i in range(len(answer_bit)):
        if answer_bit[i] != err_bit[i]:
            count +=1
            change_bit(i,answer_bit[i])

    print("#{} {}".format(test_case,count))