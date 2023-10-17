from collections import deque


def solution(n, words):
    total = len(words)
    words = deque(words)
    # print(words)
    pre = words.popleft()
    set_words = set()
    set_words.add(pre)
    while (len(words) > 0):
        next = words.popleft()
        # print('in the set??', set_words)
        # print('check the word', pre, next)
        if pre[-1] != next[0]:
            print('wp', (total - len(words)), n)
            if (total - len(words)) % n == 0:
                return [n, ((total - len(words))//n)]
            else:
                return [(total - len(words)) % n, ((total - len(words))//n)+1]
        elif next in set_words:
            print('dow', (total - len(words)), n)
            if (total - len(words)) % n == 0:
                return [n, ((total - len(words))//n)]
            else:
                return [(total - len(words)) % n, ((total - len(words))//n)+1]
        pre = next
        set_words.add(next)
    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel",
      "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["tank", "kick", "kick", "know"]))
