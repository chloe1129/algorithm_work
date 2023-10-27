def climbingLeaderboard(ranked, player):
    # Write your code here
    answer = []
    dic_rank = {}
    for i in range(len(list(set(ranked)))):
        dic_rank[i+1] = sorted(list(set(ranked)), reverse=True)[i]

    print(dic_rank)

    i = len(dic_rank)
    for j in range(len(player)):
        print('===========================')
        print('this is player', player[j])
        if player[j] >= dic_rank[1]:
            answer.append(1)
        else:
            while (True):
                if dic_rank[i] < player[j] < dic_rank[i-1]:
                    print(
                        f'111111 {i}: {dic_rank[i]}, player: {player[j]},  {i-1}: {dic_rank[i-1]}')
                    answer.append(i)
                    break
                elif player[j] < dic_rank[i]:
                    print(f'22222222 player : {player[j]}, {i}: {dic_rank[i]}')
                    answer.append(i+1)
                    break
                elif player[j] == dic_rank[i]:
                    print(
                        f'3333333333 player : {player[j]}, {i}: {dic_rank[i]}')
                    answer.append(i)
                    break
                else:
                    print(
                        f'4444444444 player : {player[j]}, {i}: {dic_rank[i]}')
                    i -= 1

    return answer


print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
