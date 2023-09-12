def solution(keymap, targets):
    result = []
    count = {}
    for lst in keymap:
        for i, pad in enumerate(lst):
            if (pad in count) and (count[pad] < i):
                pass
            else:
                count[pad] = i
    print(count)
    for a in targets:
        temp = 0
        for b in a:
            if b in count:
                temp += (count[b]+1)
            else:
                temp = -1
                break
        result.append(temp)

    return result


# print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
# print(solution(["A", "AB", "B"], ["B"]))
print(solution(["BC"], ["AC", "BC"]))
