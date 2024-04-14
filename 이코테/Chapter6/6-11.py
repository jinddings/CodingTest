N = int(input())

array = []
for i in range(N):
    input_data = input().split()
    array.append((input_data[0],input_data[1]))

array.sort(key=lambda x : x[1])

for data in array:
    print(data[0],end=' ')

