def solution(board, moves):
    answer = 0
    map = board
    basket = []
    for i in moves:
        doll = 0
        while (True):
            if doll >= len(board):
                break
            if board[doll][i-1] != 0:
                basket.append(map[doll][i-1])
                map[doll][i-1] = 0
                break
            doll += 1
        if len(basket) > 1:
            if basket[len(basket)-1] == basket[len(basket)-2]:
                basket.pop(len(basket)-1)
                basket.pop(len(basket)-1)
                answer += 2
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
