def solution(board, moves):
    ans = 0
    baguni = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                baguni.append(board[j][i-1])
                board[j][i-1] = 0
                if len(baguni) > 1:
                    if baguni[-1] == baguni[-2]:
                        baguni.pop(-1)
                        baguni.pop(-1)
                        ans += 2
                break
    return ans