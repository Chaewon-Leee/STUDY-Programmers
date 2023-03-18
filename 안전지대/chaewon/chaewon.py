def solution(board):
  changes = []
  for col, row in enumerate(board):
    for idx, element in enumerate(row):
      if element == 1:
        changes.append(change_num(idx, col))

  for change in changes:
    for row, col in change:
      if row >= len(board) or row < 0 or col >= len(board) or col < 0: pass
      else:
        board[row][col] += 1

  return sum(board, []).count(0)

def change_num(idx, col):
  changes = [[idx-1, col-1], [idx-1, col], [idx-1, col+1],
            [idx, col-1], [idx, col], [idx, col+1],
            [idx+1, col-1], [idx+1, col], [idx+1, col+1]]
  return changes

# print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1], [1, 1, 1], [1, 0, 1]]))
# print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]))
# print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))