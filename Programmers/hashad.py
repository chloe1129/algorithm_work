def solution(x):
    answer = True 
    sum = 0

    for i in range(len(str(x))):
        sum+=int(str(x)[i])

    return True if x%sum == 0 else False

what = solution(13)
print(what)