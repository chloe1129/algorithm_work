def solution(survey, choices):
    answer = ''
    num = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}

    mbti = {'RT': [0, 0], 'CF': [0, 0], 'JM': [0, 0], 'AN': [0, 0]}
    # RT CF JM AN
    # 매우동의: 7 +3, 동의: 6 +2, 약간동의:5 +1, 모르겠음:4, 약간비동의:3, 비동의:2, 매우비동의:1

    for i in range(len(survey)):
        if survey[i][0] < survey[i][1]:
            print('check survey=====', survey[i])
            if choices[i] < 4:
                print('which mbti???', survey[i][0], num[choices[i]])
                mbti[survey[i]][0] += num[choices[i]]
            elif choices[i] > 4:
                print('which mbti???', survey[i][1], num[choices[i]])
                mbti[survey[i]][1] += num[choices[i]]
            else:
                pass
        else:
            print('check survey=====', survey[i])
            if choices[i] < 4:
                print('which mbti???', survey[i][1], num[choices[i]])
                mbti[''.join(sorted(survey[i]))][1] += num[choices[i]]
            elif choices[i] > 4:
                print('which mbti???', survey[i][0], num[choices[i]])
                mbti[''.join(sorted(survey[i]))][0] += num[choices[i]]
            else:
                pass

    print(mbti)
    for i in mbti:
        if mbti[i][0] >= mbti[i][1]:
            answer += i[0]
        elif mbti[i][0] < mbti[i][1]:
            answer += i[1]

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
