import sys

bracket = list(sys.stdin.readline().strip())
total = 0
inside = 0
newarr = []
while (len(bracket) > 0):
    newarr.append(bracket.pop())
    if len(newarr) > 1:
        if [newarr[-1], newarr[-2]] == ['[', ']']:
            print('same with []', newarr, total)
            newarr.pop()
            newarr.pop()
            if inside == 0 and len(newarr) == 0:
                print('inside 0', newarr, inside)
                total += 3
            elif inside == 0 and len(newarr) > 0:
                print('inside 0 but more to go', newarr, inside)
                inside = 3
            elif inside > 0 and len(newarr) == 0:
                print('final inside', newarr, inside)
                total += (inside*3)
                inside = 0
            elif inside > 0 and len(newarr) > 0:
                print('inside but more', newarr, inside)
                inside = inside*3

        elif [newarr[-1], newarr[-2]] == ['(', ')']:
            print('same with ()', newarr, total)
            newarr.pop()
            newarr.pop()
            if inside == 0 and len(newarr) == 0:
                print('inside 0', newarr, inside)
                total += 2
            elif inside == 0 and len(newarr) > 0:
                print('inside 0 but more to go', newarr, inside)
                inside = 2
            elif inside > 0 and len(newarr) == 0:
                print('final inside', newarr, inside)
                total += (inside*2)
                inside = 0
            elif inside > 0 and len(newarr) > 0:
                print('inside but more', newarr, inside)
                inside = inside*2

if len(newarr) > 0:
    print(0)
else:
    print(total)
