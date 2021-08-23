#! usr/bin/python3

#import cgi
import connect_function as func

p_list = ["o", "x", "-"]
turn = 1
func.reset_board()

while True:
    board = func.set_piece()
    l = input("コマを落とすlineを入力、もしくはリセットを選択してください(0~6 or reset)：")
    if l == "reset":
        board = func.reset_board()
        turn = 1
    else:
        board = func.drop_piece(board, int(l), turn)
        func.record_board(board)
        turn += 1
    
    for i in range(6):
        for j in range(7):
            print(p_list[board[i][j]], end = " ")
        print()
    
    for i in range(6):
        for j in range(7):
            for d in func.dir_list:
                if (func.check_piece(board, board[i][j], j, i, d) == 4):
                    print("Brilliant!")
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break