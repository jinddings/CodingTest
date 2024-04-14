N = int(input())
data = []
for i in range(N):
    data.append(int(input()))

data = sorted(data,reverse=True)

for i in range(N):
    print(data[i],end=' ')