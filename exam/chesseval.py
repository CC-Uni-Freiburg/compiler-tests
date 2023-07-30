# Author: Alexander Pfefferle
#in=
#golden=0-7
a=[[4, 1, 0, 0, 0, 0, 7, 10],
  [2, 1, 0, 0, 0, 0, 7, 8],
  [3, 1, 0, 0, 0, 0, 7, 9],
  [5, 1, 0, 0, 0, 0, 7, 11],
  [6, 1, 0, 0, 0, 0, 7, 12],
  [3, 1, 0, 0, 0, 0, 7, 9],
  [2, 1, 0, 0, 0, 0, 7, 8],
  [4, 1, 0, 0, 0, 0, 7, 10]]

def eval_board(board: list[list[int]]) -> int:
  v=0
  i=0
  while i<len(board):
    j=0
    while j<len(board[i]):
      p=board[i][j]%6
      c=(-2*(board[i][j]//6))+1
      if p==1:v=v+1*c
      if p==4:v=v+5*c
      if p==2:v=v+3*c
      if p==3:v=v+3*c
      if p==5:v=v+9*c
      j=j+1
    i=i+1 
  return v

print(eval_board(a))
a[3][0]=0
a[0][6]=0
a[1][6]=0
print(eval_board(a))
