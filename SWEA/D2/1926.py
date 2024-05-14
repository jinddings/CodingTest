from collections import deque
N = int(input())
queue = deque()

for i in range(1,N+1):
    queue.append(i)

def clab(num):
    count = 0
    str_digit = list(str(num))
    for item in str_digit:
        digit = int(item)
        if digit%3 == 0 and digit != 0:
            count += 1
    return count

while queue:
    num = queue.popleft()
    clab_count = clab(num)
    if clab_count == 0:
        print(num,end=' ')
    else:
        print(clab_count*'-',end=' ')


