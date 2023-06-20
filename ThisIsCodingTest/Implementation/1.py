def solution():
    n = int(input())
    x, y = 1, 1
    data = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    step_types = ['L', 'R', 'U', 'D']

    for step in data:
        for i in range(len(step_types)):
            if step == step_types[i]:
                nx = x+dx[i]
                ny = y+dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

    return x, y

print(solution())