import heapq
import sys
input = sys.stdin.readline

N = int(input())

min_heap = []
max_heap = []
weight = -1

for _ in range(N):
    input_num = int(input())

    if input_num != 0:
        if input_num < 0 :
            heapq.heappush(max_heap,weight*input_num)
        else:
            heapq.heappush(min_heap,input_num)
    else:
        if not min_heap and not max_heap:
            print(0)
        elif not min_heap:
            print(weight*heapq.heappop(max_heap))
        elif not max_heap:
            print(heapq.heappop(min_heap))
        else:
            if max_heap[0] == min_heap[0]:
                print(weight*heapq.heappop(max_heap))
            elif max_heap[0] < min_heap[0]:
                print(weight*heapq.heappop(max_heap))
            else:
                print(heapq.heappop(min_heap))





