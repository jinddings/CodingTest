decode = []
T = int(input())

for i in range(ord('Z') - ord('A') + 1):
    decode.append(chr(ord('A') + i))

for i in range(ord('z') - ord('a') + 1):
    decode.append(chr(ord('a') + i))

for i in range(ord('9') - ord('0') + 1):
    decode.append(chr(ord('0') + i))

decode.append('+')
decode.append('-')

for test_case in range(1, T + 1):
    res = ''
    arr = list(input())

    for i in range(len(arr)):
        num = decode.index(arr[i])
        bin_num = str(bin(num))[2:]

        while len(bin_num) < 6:
            bin_num = '0' + bin_num

        res += bin_num

    result = ''
    for j in range((len(arr) * 6) // 8):
        number = int(res[j * 8: j * 8 + 8], 2)
        result += chr(number)

    print("#{} {}".format(test_case,result))