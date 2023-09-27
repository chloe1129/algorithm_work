import re


def solution(new_id):
    # level1
    text = new_id.lower()

    # level2
    text = re.sub(r'[~!@#$%^&*\(\)=+\[\{\]\}:?,<>/]', '', text)

    # level3
    text = re.sub(r'\.+', '.', text)

    # level 4
    while (len(text) > 0):
        if text[0] == '.' and text[-1] == '.':
            text = text[1:-1]
            break
        elif text[-1] == '.':
            text = text[:-1]
            break
        elif text[0] == '.':
            text = text[1:]
            break
        else:
            break

    # level 5
    if text == '':
        text += 'a'

    # level 6
    if len(text) >= 16:
        text = text[:15]
        if text[-1] == '.':
            text = text[:-1]

    # level 7
    while (len(text) < 3):
        text += text[-1]
        if len(text) > 2:
            break
    return text


print(solution("...!!@BaT#*..y.abcdefghijklm."))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
