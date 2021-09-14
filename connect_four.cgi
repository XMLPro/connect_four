#! /usr/bin/python3

import cgi
import connect_function as func

print("Content-Type: text/html\n")
htmlText = ""
file = "game_display.html"
flag = 0
victory = 0


with open(file) as f:
  content = f.readlines()
board, turn = func.set_piece()

form = cgi.FieldStorage()
l = form.getvalue("number")
if l != None:
    l = int(l)

if l == -1 or l == None:
  board = func.reset_board()
else:
  board = func.drop_piece(board, l, turn)
  func.record_board(board, turn)

for i in range(6):
  for j in range(7):
    for d in func.dir_list:
      if (func.check_piece(board, board[i][j], j, i, d) == 4):
        end_txt = "<h2>Thank You For Playing!!!</h2>"
        victory = 1
        break
    else:
      continue
    break
  else:
    continue
  break

for txt in content:
  if "/table" in txt:
    flag = 0
  if flag:
    continue

  if 'id="result' in txt:
    if turn % 2:
      htmlText += '<h3 id="result_r">赤の番です</h3>'
    else:
      htmlText += '<h3 id="result_y">黄の番です</h3>'
  elif 'id="board' in txt:
    htmlText += txt
    flag = 1
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
  else:
    htmlText += txt
    if "h1" in txt and victory:
        htmlText += end_txt

print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))
