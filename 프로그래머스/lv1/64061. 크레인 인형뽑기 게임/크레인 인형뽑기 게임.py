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