import sys
input = sys.stdin.readline

N,M = map(int,input().split())

S = []
for _ in range(N):
    input_str = input().rstrip()
    S.append(input_str)

count = 0
for _ in range(M):
    input_str = input().rstrip()
    if input_str in S:
        count +=1

print(count)



