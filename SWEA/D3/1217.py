def power(N,M):
    if M == 0:
        return 1
    return N*power(N,M-1)

for _ in range(10):
    T = int(input())
    N,M = map(int,input().split())

    power(N,M)
    print("#"+str(T)+" "+str(power(N,M)))
