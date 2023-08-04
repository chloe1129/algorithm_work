def solution(keymap, targets):
    answer = [0]*len(keymap)
    result = []
    for i in keymap:
        answer[keymap.index(i)] = dict()
        for j in range(len(i)):
            answer[keymap.index(i)][j] = i[j]
    for i in targets:
        a = 0
        for j in i:
            result.append(list(answer[0].keys())[
                          list(answer[0].values()).index(j)])

    return result


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
