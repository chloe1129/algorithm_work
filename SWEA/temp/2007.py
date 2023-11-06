from collections import deque
import itertools

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word = deque(list(input().strip()))
    repeat = word.popleft()
    idx = 0
    while (True):
        # print('repeat', repeat, list(itertools.islice(word, len(repeat))))
        if repeat == ''.join(list(itertools.islice(word, len(repeat)))):
            break
        else:
            temp = word.popleft()
            repeat += temp
    print(f'#{test_case} {len(repeat)}')
