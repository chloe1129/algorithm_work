def solution(s, skip, index):
    answer = ''

    for i in s:
        j = index
        char = ord(i)
        while (j != 0):
            char += 1
            if char > ord('z'):
                char = char - ord('z') + ord('a')-1

            if chr(char) in skip:
                continue
            j -= 1


        answer += chr(char)

    return answer