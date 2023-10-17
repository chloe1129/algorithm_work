def solution(brown, yellow):
    add = brown//2+2
    multi = brown + yellow
    for i in range(add):
        # print(i, add-i, i*(add-i))
        if i*(add-i) == multi:
            return [max(i,add-i),min(i,add-i)]
    return 