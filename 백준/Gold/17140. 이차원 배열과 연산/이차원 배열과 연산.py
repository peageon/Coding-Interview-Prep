from collections import Counter, defaultdict
from itertools import chain
def check(board, r, c, k):
  if check_bounds(board, r,c) and board[r-1][c-1] == k:
    return True
  return False

def check_bounds(board, r,c):
  if len(board) >= r and len(board[0]) >= c:
    return True
  return False

def applyC(board):
  #transform?
  t_board = []
  for i in range(len(board[0])):
    column = []
    for j in range(len(board)):
      column.append(board[j][i])
    t_board.append(column)
  t_board = applyR(t_board)
  #transform back
  applied_board = [[] for _ in range(len(t_board[0]))]
  for j in range(len(t_board)):
    for i in range (len(t_board[0])):
      applied_board[i].append(t_board[j][i])
  return applied_board

def applyR(board):
  largest = 0
  for i in range(len(board)):
    board[i] = sort_this(board[i])
    if largest < len(board[i]):
      largest = len(board[i])
  #sorted
  for i in range(len(board)):
    board[i] = board[i] + ([0] * (largest-len(board[i])))
  #added 0s
  return board


def sort_this(line):
  counted = Counter(line) #각각의 수가 몇번 나왔는지
  if 0 in counted:
    del counted[0]
  tuple_list = [[k,v] for k,v in counted.items()]
  sorted_tuple_list = sorted(tuple_list, key=sort_helper)
  flattened = list(chain.from_iterable(sorted_tuple_list))
  return flattened

def sort_helper(comp):
  return (comp[1], comp[0])


r,c,k = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(3)]

second = 0

if(check(board, r, c, k)):
  print(0)
  exit()

while second < 100:
  second += 1
  if(len(board) >= len(board[0])):
    board = applyR(board)
  else:
    board = applyC(board)
  
  if(check(board, r, c, k)):
    print(second)
    exit()
print(-1)
exit()
  
