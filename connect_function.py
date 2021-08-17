dir_list = ["under", "right", "r_dia", "l_dia"]

def set_piece():
    with open("./board.txt") as f:
        board = [list(map(int, s.strip())) for s in f.readlines()]
    return board


def drop_piece(board, line, turn):
    for i in range(board):
        if board[5-i][line] != 2:
            board[5-i][line] = turn//2
    return board
            
def record_board(board):
    r_board = [list(map(str, s)) for s in board]
    with open(".board.txt", mode='w') as f:
        txt = ""
        for i in r_board:
            for j in i:
                txt += j
            txt += "\n"
        f.write(txt)

def check_piece(board, pl, x_place, y_place, direction):
    if (x_place < -1 or 6 < x_place) or (y_place < -1 or 5 < y_place):
        return 0

    else if (board[y_place][x_place] != pl):
        return 0

    else:
        if (direction == dir_list[0]):
            return 1 + check_piece(board, board[y_place+1][x_place]), x_place, y_place+1, dir_list[0])
        else if (direction == dir_list[1]):
            return 1 + check_piece(board, board[y_place][x_place+1]), x_place+1, y_place, dir_list[1])
        else if (direction == dir_list[2]):
            return 1 + check_piece(board, board[y_place+1][x_place+1]), x_place+1, y_place+1, dir_list[2])
        else if (direction == dir_list[3]):
            return return 1 + check_piece(board, board[y_place+1][x_place-1]), x_place-1, y_place+1, dir_list[3])

def reset_board():
    board = [[2]*7 for s in range(6)]
    record_board(board)
    return board