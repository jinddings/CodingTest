stack = []
arr = enumerate(input())
stack = []
answer = 0
tmp = 1
for a in arr:
    idx, item = a
    if item == '(' :
        stack.append((idx,item))
        tmp *= 2
    elif item == '[':
        stack.append((idx,item))
        tmp *= 3
    else:
        if not stack:
            answer = 0
            break
        pidx,p = stack.pop()
        if p == '(' and  item == ']':
            answer = 0
            break
        if p == '[' and item == ')':
            answer = 0
            break
        if item == ')':
            if idx-pidx == 1:
                answer += tmp
            tmp //= 2
        else :
            if idx-pidx == 1:
                answer += tmp
            tmp //= 3


if stack:
    print(0)
else:
    print(answer)




