import string

encode = list(string.ascii_uppercase +
              string.ascii_lowercase + string.digits + '+/')
encode = {num: i for i, num in enumerate(encode)}
# print(encode)
T = int(input())
for test_case in range(1, T + 1):
    string = list(input().strip())
    for i in range(len(string)):
        string[i] = bin(encode[string[i]])[2:].zfill(6)

    # print(string, len(''.join(string)))
    result = ''
    a = 0
    string = ''.join(string)
    for _ in range(len(string)//8):
        result += chr(int(string[a:a+8], 2))
        a += 8
    print('#'+str(test_case)+' '+result)
