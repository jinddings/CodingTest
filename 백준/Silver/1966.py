from collections import deque

T = int(input())

for _ in range(T):
    M,target_idx = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    count = 0

    while queue:
        biggest = max(queue)
        cur_p = queue.popleft()
        target_idx -= 1

        if cur_p == biggest:
            count +=1
            if target_idx<0:
                print(count)
                break
        else:
            queue.append(cur_p)
            if target_idx<0:
                target_idx = len(queue)-1


