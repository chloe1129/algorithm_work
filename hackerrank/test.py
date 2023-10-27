import bisect


def solution(n, k, x, y):
    answer = 0
    if n == 1:
        return -1

    lst = []
    for a in range(n):
        lst.append([x[a], y[a]])
    lst.sort(key=lambda x: x[0])
    x.sort()
    # print(lst, x)

    i = 0
    # print(bisect.bisect_left(x, 84))
    while (True):
        j = bisect.bisect_left(x, x[i]+k)
        print('this is j', x, x[i], j, x[j])
        if j < n:
            answer = max(answer, lst[i][1] + lst[j][1])

        j += 1

        if j == n:
            i += 1
            j = i+1

        if i >= n-1:
            break

    if answer == 0:
        return -1
    else:
        return answer


print(solution(5, 10,
               [75, 84, 82, 95, 90],
               [88, 90, 72, 80, 83]))
