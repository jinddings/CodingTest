T = int(input())
def solution(i,sum):
    global count
    if sum == K :
        count +=1
        return
    if i == N:
        return
    solution(i+1,sum)
    solution(i+1,sum+nums[i])

for test_case in range(1,T+1):
    N,K = map(int,input().split())
    nums = list(map(int,input().split()))

    count = 0
    solution(0,0)

    print("#{} {}".format(test_case,count))


