def solution(lottos, win_nums):

    score = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    answer = []
    lottos = sorted(lottos)
    win_nums = sorted(win_nums)
    print(lottos, win_nums)

    zeros = 0
    for i in lottos:
        if i == 0:
            zeros += 1
        else:
            for j in win_nums:
                if i == j:
                    answer.append(i)
                    win_nums.remove(j)
    print(win_nums, answer, zeros)

    return [score[len(answer)+zeros], score[len(answer)]]