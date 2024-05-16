T = int(input())

def pascal(num):
    list = []
    if num == 1:
        result[num] = [1]
        return
    elif num == 2:
        pascal(num-1)
        result[num] = [1,1]
        return
    else:
        pascal(num-1)
        arr = result[num-1]
        list.append(1)
        for a in range(len(arr) - 1):
            list.append(arr[a] + arr[a + 1])
        list.append(1)

    result[num] = list
    return



for test_case in range(1,T+1):
  N = int(input())
  result = {}
  pascal(N)

  print("#{}".format(test_case))
  for i in range(1,N+1):
      print(*result[i])
