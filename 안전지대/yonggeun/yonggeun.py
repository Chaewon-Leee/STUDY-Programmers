def solution(board):
    bomb_coords = []
    dangerous_coords = []
    for i, row in enumerate(board):
        for j, point in enumerate(row):
            if point == 1:
                bomb_coords.append((i, j))
                dangerous_coords.append((i, j))
    for coord in bomb_coords:
        x, y = coord
        # 좌표 주변 좌표들 구하기
        neighbors = [(x-1, y+1), (x, y+1), (x+1, y+1), (x-1, y), (x+1, y), (x-1, y-1), (x, y-1), (x+1, y-1)]
        # 주변 좌표들 중에 board 내부에 있는 좌표들만 추가
        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                dangerous_coords.append(neighbor)

    return len(board) * len(board[0]) - len(list(set(dangerous_coords)))

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
print(solution(board))