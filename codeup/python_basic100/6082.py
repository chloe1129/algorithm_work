a = input()

for i in range(1,1+int(a)):
    if ('3' in list(str(i))) or '6' in list(str(i)) or '9' in list(str(i)):
        print('X')
    else:
        print(i)
