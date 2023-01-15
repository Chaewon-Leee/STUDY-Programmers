def solution(keyinput, board):
    width = board[0] // 2
    length = board[1] // 2

    location = [0, 0]

    for direction in keyinput:
      next_location = move(location, direction)

      if abs(next_location[0]) > width or abs(next_location[1]) > length:
        pass
        # print(f"next_location : {next_location}")
      else:
        location = next_location
        # print(f"location : {location}")
    return location

def move(location, direction):
  movement_dic = {"left": [location[0] - 1, location[1]], "right": [location[0] + 1, location[1]],
                    "up": [location[0], location[1] + 1], "down": [location[0], location[1] - 1]}
  return movement_dic[direction]

# print(solution(["left", "right", "up", "right", "right"], [11, 11]))
# print(solution(["down", "down", "down", "down", "down"], [7, 9]))
# print(solution(["left"], [7, 9]))