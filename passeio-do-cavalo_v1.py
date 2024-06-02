def is_safe(board, x, y, N):
    return x >= 0 and y >= 0 and x < N and y < N and board[x][y] == -1

def knight_tour(N):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    pos = 1
    if not knight_tour_util(board, 0, 0, move_x, move_y, pos, N):
        print("Não há solução")
    else:
        print_board(board)

def knight_tour_util(board, x, y, move_x, move_y, pos, N):
    if pos == N * N:
        return True
    for i in range(8):
        new_x = x + move_x[i]
        new_y = y + move_y[i]
        if is_safe(board, new_x, new_y, N):
            board[new_x][new_y] = pos
            if knight_tour_util(board, new_x, new_y, move_x, move_y, pos + 1, N):
                return True
            board[new_x][new_y] = -1
    return False

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(f"{board[i][j]:2d}", end=" ")
        print()

# Exemplo de uso
N = 8
knight_tour(N)
