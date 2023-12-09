import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    order = str(sys.stdin.readline().strip())
    if len(order) >= 6:
        order, num = order.split(' ')

    if order == 'push':
        arr.append(num)
    elif order == 'pop':
        if len(arr) == 0:
            print('-1')
        else:
            a = arr.pop()
            print(a)
    elif order == 'size':
        print(len(arr))
    elif order == 'empty':
        if len(arr) == 0:
            print('1')
        else:
            print('0')

    elif order == 'top':
        if len(arr) == 0:
            print('-1')
        else:
            print(arr[-1])
