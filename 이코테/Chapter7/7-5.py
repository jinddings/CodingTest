def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) //2

        if array[mid] == target :
            return mid
        elif array[mid] > target :
            end = mid -1
        else :
            start = mid +1

    return None


N = int(input())
array = list(map(int,input().split()))
array.sort()

M = int(input())
target_array = list(map(int,input().split()))

for i in range(M):
    result = binary_search(array, target_array[i],0,len(array))
    if result is None:
        print('no')
    else :
        print('yes')




