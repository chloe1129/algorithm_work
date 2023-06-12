import re


def recure(bab):
    words = [
        "aya",
        "ye",
        "woo",
        "ma"
    ]
    for n, i in enumerate(words):
        if i in bab:
            print("1111111111111111111", i, bab)
            ind = bab.find(i)
            print("indexxxxxxxxx", ind)
            i = i[0:ind]+' '+i[ind+len(i):len(bab)]
            print("222222222222222", n, i)
        if n == 4:
            return 1

    return i


def solution(babbling):

    answer = 0
    for i in babbling:
        print("===========", recure(i))
    return answer


print(solution(["aya", "yee", "u", "maa"]))
