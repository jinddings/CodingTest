import heapq
N = int(input())

queue = []
heapq.heapify(queue)

for _ in range(N):
    arr = list(map(int,input().split()))
    for item in arr :
        if len(queue) < N :
            heapq.heappush(queue,item)
        else:
            if queue[0] < item:
                heapq.heappop(queue)
                heapq.heappush(queue,item)


print(queue[0])





