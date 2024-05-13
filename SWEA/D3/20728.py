

import math
T = int(input())
for test_case in range(T):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort()

    min = math.inf
    for i in range(N-K+1):
        if min > (arr[i+K-1] - arr[i]):
            min = arr[i+K-1] - arr[i]

    print("#{} {}".format(test_case+1,min))