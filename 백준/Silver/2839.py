
def solution(n):
    result = 0
    sugar = n

    while sugar >= 0:
        if sugar % 5 == 0:
            result += sugar//5
            print(result)
            return
        sugar -=3
        result +=1
    else:
        print(-1)
    return

N = int(input())
solution(N)