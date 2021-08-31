#! usr/bin/python3

import cgi
import connect_function as func

p_list = ["circle_r", "circle_y", "circle"]
#turn = get------

board = func.set_piece()
#l = get------
if l == "reset":
    board = func.reset_board()
    turn = 1
else:
    board = func.drop_piece(board, int(l), turn)
    func.record_board(board)
    turn += 1

htmlText = """
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8"/>
    <title>コネクトフォー</title>
    <link rel="stylesheet" type="text/css" href="display.css">
    <script type="text/javascript" src="display.js"></script>
  </head>
  <body>
    <h1>コネクトフォー</h1>
    <h3 id="result_r">赤の番です</h3>
    <table id="push_table">
      <tr>
        <td class="push_td"><span class="push" id="push_col0" type="submit"><br>PUSH!<br>↓</span></td>
        <td class="push_td"><span class="push" id="push_col1" type="submit"><br>PUSH!<br>↓</span></td>
        <td class="push_td"><span class="push" id="push_col2" type="submit"><br>PUSH!<br>↓</span></td>
        <td class="push_td"><span class="push" id="push_col3" type="submit"><br>PUSH!<br>↓</span></td>
        <td class="push_td"><span class="push" id="push_col4" type="submit"><br>PUSH!<br>↓</span></td>
        <td class="push_td"><span class="push" id="push_col5" type="submit"><br>PUSH!<br>↓</span></td>
        <td class="push_td"><span class="push" id="push_col6" type="submit"><br>PUSH!<br>↓</span></td>
      </tr>
    </table>
    <form action="" name="dropnum" method="POST">
      <input id="post_num" type="hidden" name="number" value="">
    </form>
    <table id="board" border="1">"""

for i in range(6):
    htmlText += """<tr>"""
    for j in range(7):
        if board[i][j] == 0:
            htmlText += """<td class="circle_td"><span class="circle_r">&emsp;</span></td>"""
        elif board[i][j] == 1:
            htmlText += """<td class="circle_td"><span class="circle_y">&emsp;</span></td>"""
        elif board[i][j] == 2:
            htmlText += """<td class="circle_td"><span class="circle">&emsp;</span></td>"""
    htmlText += """</tr>"""

for i in range(6):
    for j in range(7):
        for d in func.dir_list:
            if (func.check_piece(board, board[i][j], j, i, d) == 4):
                #htmlText += """  """
                break
        else:
            continue
        break
    else:
        continue
    break

htmlText += """
</table>
    <br>
    <form action="" method="POST">
      <div id="reset_button">
        <input type="hidden" name="reset" value="reset">
        <input type="submit" value="リセット">
      </div>
    </form>
  </body>
</html>"""