a, b, c = map(int, input().split())


def recur(a, b):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (recur(a, b//2)**2) % c
    else:
        return ((recur(a, b//2)**2)*a) % c


print(recur(a, b))