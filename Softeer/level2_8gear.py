import sys

data = list(map(str, sys.stdin.readline().split()))

data = ''.join(data)
if data == '12345678':
    print('ascending')
elif data == '87654321':
    print('descending')
else:
    print('mixed')
