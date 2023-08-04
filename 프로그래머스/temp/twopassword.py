def solution(s, skip, index):
    answer = ''

    for i in s:
        j = index
        char = ord(i)
        while (j != 0):
            char += 1
            if char > ord('z'):
                print("11111111111", char)
                char = char - ord('z') + ord('a')-1

            if chr(char) in skip:
                continue
            j -= 1
            print("22222222222", char)

        print("333333333333", char)

        print("index", j)
        answer += chr(char)

    return answer


print(solution("aukks", "wbqd",	5))
print(solution("y", "baz",	1))
