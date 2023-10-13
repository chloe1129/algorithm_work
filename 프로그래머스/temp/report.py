def solution(id_list, report, k):
    answer = []
    user_report = {}
    user_warn = {}
    yes_warn = []
    for i in range(len(id_list)):
        user_report[id_list[i]] = []  # 사용자가 신고한 사람 목록 저장
        user_warn[id_list[i]] = 0  # 사용자가 신고당한 횟수
        answer.append(0)

    for i in range(len(report)):
        reporter, reporti = report[i].split(' ')

        if reporti not in user_report[reporter]:
            user_warn[reporti] += 1

        if reporti not in user_report[reporter]:
            user_report[reporter].append(reporti)
    print(user_report, user_warn)

    for i in range(len(id_list)):
        if user_warn[id_list[i]] >= k:
            yes_warn.append(id_list[i])
    print(yes_warn)

    for i in range(len(yes_warn)):
        for j in range(len(id_list)):
            if yes_warn[i] in user_report[id_list[j]]:
                answer[j] += 1
    return answer


print(solution(["ab", "b"], ["ab b"], 1))
