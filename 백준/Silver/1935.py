from collections import deque
N = int(input())
op = '+-*/'
dec_dict = {}
input_arr = list(map(str,input()))


for i in range(N):
    dec_dict[chr(ord('A')+i)] = int(input())

stack = []

for item in input_arr:
    if item not in op:
        stack.append(dec_dict[item])
    else :
        b = stack.pop()
        a = stack.pop()
        if item == '+':
            stack.append(a+b)
        elif item == '-':
            stack.append(a-b)
        elif item == '*':
            stack.append(a*b)
        elif item == '/':
            stack.append(a/b)

print("{:.2f}".format(stack.pop()))