T = 10

for test_case in range(1,T+1):
    N = int(input())
    origin_nums = list(map(str,input().split()))
    M = int(input())
    commands = list(map(str,input().split()))

    list_commands = []

    for i in range(len(commands)):
        if commands[i] == 'I':
            x = int(commands[i+1])
            y = int(commands[i+2])

            for j in range(y):
                origin_nums.insert(x+j,commands[i+3+j])




    print("#{}".format(test_case),end=" ")
    print(*origin_nums[:10])
