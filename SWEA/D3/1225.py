from collections import deque

T = 11

for test_case in range(1,T):
    N = int(input())
    nums = deque(list(map(int,input().split())))

    flag = True
    count = 1
    while flag:
        item = nums.popleft() - count
        if item <= 0:
            item = 0
            nums.append(item)
            flag = False
        else:
            nums.append(item)
            if count < 5:
                count +=1
            else:
                count = 1

    print("#{} ".format(test_case),end='')
    print(*nums)
