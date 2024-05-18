from collections import deque

N = int(input())
nums_list = list(map(int,input().split()))
nums_deque = deque(enumerate(nums_list))

ans = []
while nums_deque:
    idx,num = nums_deque.popleft()
    ans.append(idx+1)

    if num > 0 :
        nums_deque.rotate(-(num-1))
    else :
        nums_deque.rotate(-(num))

print(*ans)