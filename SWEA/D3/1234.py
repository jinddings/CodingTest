def find_idx():
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return i
    return -1

for test_case in range(1,11):
    N, arr = map(str,input().split())
    N = int(N)
    arr = list(arr)

    while find_idx() != -1:
        idx = find_idx()
        arr.pop(idx)
        arr.pop(idx)


    print("#{}".format(test_case),end=" ")
    print("".join(arr))


