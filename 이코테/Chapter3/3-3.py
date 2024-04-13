n,m = map(int, input().split())

for i in range(n):
    min_vals = []
    row = list(map(int,input().split()))
    min_vals.append(min(row))

print(max(min_vals))
