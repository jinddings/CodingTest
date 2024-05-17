from collections import deque
import heapq

T = int(input())

def solution():
    while queue:
        for i in range(len(queue)):
            queue[i] = queue[i] - M

        popLen = len(queue) if len(queue) < K else K
        for _ in range(popLen):
            item = heapq.heappop(queue)
            if item < 0 :
                return False
    return True

for test_case in range(1,T+1):
    N,M,K = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    heapq.heapify(queue)
    print("#{} {}".format(test_case,"Possible" if solution() else "Impossible"))
