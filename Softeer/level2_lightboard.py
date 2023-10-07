import sys

n = int(input())

data = {
    '0': '1111110',
    '1': '0110000',
    '2': '1101101',
    '3': '1111001',
    '4': '0110011',
    '5': '1011011',
    '6': '1011111',
    '7': '1110010',
    '8': '1111111',
    '9': '1111011',
    ' ': '0000000'
}


for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    total = 0
    a = ' '*(5-len(str(a)))+str(a)
    b = ' '*(5-len(str(b)))+str(b)
    print('abababab', a, b, type(a), type(b))
    for i in range(5):
        for j in range(7):
            print(data[a[i]][j], data[b[i]][j])
            if (data[a[i]][j] != data[b[i]][j]):
                total += 1
    print(total)
