import sys
import heapq

inf = sys.maxsize
graph = {}

V, E = map(int,input().split())
start_v = int(input())

for i in range(1,V+1):
    graph[i] = []

for i in range(E):
    start, end , weight = map(int,input().split())
    graph[start].append((weight,end))

distances = [inf] * (V+ 1)

def dijkstra(graph,start_v):
    hpq = []
    heapq.heappush(hpq,(0,start_v))
    distances[start_v] = 0
    while hpq:
        cur_d, cur_v = heapq.heappop(hpq)
        for next_cost , next_v in graph[cur_v]:
            next_d = cur_d + next_cost
            if next_d < distances[next_v]:
                heapq.heappush(hpq,(next_d,next_v))
                distances[next_v] = next_d



dijkstra(graph,start_v)

for i in range(1,V+1):
    print("INF" if distances[i] == inf else str(distances[i]))


