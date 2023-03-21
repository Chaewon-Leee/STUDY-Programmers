def solution(lines):
    points = []
    duplicates = []
    answer = 0
    for line in lines:
        for point in range(line[0], line[1] + 1):
            if point in points:
                duplicates.append(point)
            points.append(point)
            if len(points) > 2:
                if points[-2] == points[-1]:
                    # points.remove(points[-1])
                    duplicates.remove(points[-1])

    if duplicates == []:
        return 0
    
    result = []
    current_group = []

    for i in range(len(duplicates)):
        current_group.append(duplicates[i])
        if i == len(duplicates) - 1 or duplicates[i+1] - duplicates[i] != 1:
            if len(current_group) > 1:
                result.append(current_group)
            current_group = []
    for i in len(result):
        if result[i] in result[i+1]:
            return max(result[i+1]) - min(result[i+1])
        elif result[i+1] in result[i]:
            return max(result[i]) - min(result[i])


lines = [[0, 5], [3, 9], [1, 10]]
print(solution(lines))