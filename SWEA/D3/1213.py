T = 10

for test_case in range(1,T+1):
    N = input()
    target = input()
    input_str = input()

    print("#{} {}".format(test_case,input_str.count(target)))