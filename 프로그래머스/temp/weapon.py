def solution(number, limit, power):

    a = 1
    for i in range(2, number+1):
        b = yaksoo(i, limit, power)
        a += b

    return a


def yaksoo(number, limit, power):
    a = 0
    for i in range(1, int(number**(1/2))+1):
        if number % i == 0:
            if i == number//i:
                a += 1
            else:
                a += 2
        if a > limit:
            return power
    return a


print(solution(10, 3, 2))
