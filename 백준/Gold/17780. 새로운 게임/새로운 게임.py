N, K = map(int, input().split())

board_colour = []
for i in range(N):
  board_colour.append(list(map(int,input().split())))

board_soldiers = [[[0] for _ in range(N)] for _ in range(N)]

soldiers = []
for i in range(K):
  soldier = list(map(int, input().split()))
  row = soldier[0] - 1
  col = soldier[1] - 1
  board_soldiers[row][col] = [i+1]
  soldier[0] = row
  soldier[1] = col
  soldiers.append(soldier)

#now we have something like soldiers = [[2,1,1],[3,2,3],[2,2,1],[4,1,2]] with
#each index representing the number of the soldier
  
drow = [0, 0, 0, -1, 1]
dcol = [0, 1, -1, 0, 0]
reverse_direction = {1:2, 2:1, 3:4, 4:3}

def is_valid(row, col):
  global N
  if 0 <= row < N and 0 <= col < N:
    return True
  return False
  

def take_turn():
  global board_colour, board_soldiers, soldiers, drow, dcol, reverse_direction
  for i in range(len(soldiers)):
    soldier = soldiers[i]
    row = soldier[0]
    col = soldier[1]
    direction = soldier[2]

    loc = board_soldiers[row][col]
    #if the locations first item is not the current soldier then skip
    if loc[0]-1 != i:
      continue

    next_row, next_col = row + drow[direction], col + dcol[direction]

    def white_red():
        if board_colour[next_row][next_col] == 1:
          board_soldiers[row][col].reverse()
        #extend all the soldiers stacked in current one to the soldiers in the next
        #change row, col for all the soldiers stacked in the curret one
        if board_soldiers[next_row][next_col] == [0]:
          board_soldiers[next_row][next_col] = board_soldiers[row][col]
        else:
          board_soldiers[next_row][next_col].extend(board_soldiers[row][col])
        if len(board_soldiers[next_row][next_col]) >= 4:
          return True
        for soldier_num in board_soldiers[row][col]:
          soldiers[soldier_num - 1][0] = next_row
          soldiers[soldier_num - 1][1] = next_col
        board_soldiers[row][col] = [0]
    if not is_valid(next_row, next_col) or board_colour[next_row][next_col] == 2:
      reversed_direction = reverse_direction[soldiers[i][2]]
      soldiers[i][2] = reversed_direction
      next_row, next_col = row + drow[reversed_direction], col + dcol[reversed_direction]
      if is_valid(next_row, next_col) and board_colour[next_row][next_col] in {0,1}:
        if white_red():
          return True
    elif board_colour[next_row][next_col] in {0,1}:
      if white_red():
        return True
    
  return False
    
turn = 0
while turn <= 1000:
  turn += 1
  if take_turn():
    print(turn)
    exit(0)
print(-1)
