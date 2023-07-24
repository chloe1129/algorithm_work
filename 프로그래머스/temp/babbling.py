def solution(bab):
    answer = 0
    for i in bab:
        word = str(i)
        for j in ['aya', 'ye', 'woo', 'ma']:
            if j*2 not in word:
                word = word.replace(j, '_'*len(j))
        if word == '_'*len(word):
            answer += 1

    return answer


print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
