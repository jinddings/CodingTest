import heapq
import sys
input = sys.stdin.readline

heap = []
heapq.heapify(heap)

N = int(input())

weight = -1
for _ in range(N):
    num = int(input())
    if num > 0 :
        heapq.heappush(heap,weight*num)
    else :
        #비어있는 경우
        if not heap:
            print(0)
        else :
            print(heapq.heappop(heap)*weight)
