def solution():
    n, m = map(int, input().split())
    x, y, watching = map(int, input().split())
    MAP = []
    for i in range(n):
        MAP.append(list(map(int, input().split())))
    heading_type = [0, 1, 2, 3]
    MAP[x][y] = 1
    ground_count = 1
    rotation_count = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while True:
        heading_target = heading_type[heading_type.index(watching) - 1]
        nx = x + dx[heading_type.index(heading_target)]
        ny = y + dy[heading_type.index(heading_target)]
        if MAP[nx][ny] == 0:
            MAP[nx][ny] = 1
            x, y = nx, ny
            ground_count += 1
            rotation_count = 0
            watching = heading_target
        else:
            rotation_count += 1
            watching = heading_target

        if rotation_count == 4:
            nx = x - dx[heading_type.index(heading_target)]
            ny = y - dy[heading_type.index(heading_target)]

            if MAP[nx][ny] == 0:
                x, y = nx, ny
                watching = heading_target
            else:
                break
            rotation_count = 0

    return ground_count



print(solution())