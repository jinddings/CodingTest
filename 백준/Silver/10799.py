stack = []
input_Arr = list(input())

answer = 0

idx = 0
for idx in range(len(input_Arr)):
    if input_Arr[idx] == '(':
        stack.append('(')
    elif input_Arr[idx] == ')':
        stack.pop()
        if input_Arr[idx-1] == '(':
            answer += len(stack)
        else:
            answer += 1

print(answer)