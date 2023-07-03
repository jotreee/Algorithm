import sys

input = sys.stdin.readline

N = int(input().strip())
paint = list(list(input().strip()) for _ in range(N))

rgb = list([0] * N for _ in range(N))
rb = list([0] * N for _ in range(N))

color = ''
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
rgb_num = 0
rb_num = 0

for i in range(N):
    if i > 0:
        color = paint[i - 1][0]
    for j in range(N):
        if paint[i][j] != color:
            if rb[i][j] == 0 and paint[i][j] == 'B':
                rb_num += 1
                rb_area = [[i, j]]
                rb[i][j] = rb_num
                while True:
                    appended = 0
                    for y, x in rb_area:
                        for k in range(4):
                            if (0 <= x + dr[k] < N and 0 <= y + dc[k] < N) and (rb[y + dc[k]][x + dr[k]] == 0) and paint[y + dc[k]][x + dr[k]] == 'B':
                                rb[y + dc[k]][x + dr[k]] = rb_num
                                rb_area.append([y + dc[k], x + dr[k]])
                                appended = 1
                    if appended == 0:
                        break

            elif rb[i][j] == 0 and color != ('R' or 'G'):
                rb_num += 1
                rb_area = [[i, j]]
                rb[i][j] = rb_num
                while True:
                    appended = 0
                    for y, x in rb_area:
                        for k in range(4):
                            if (0 <= x + dr[k] < N and 0 <= y + dc[k] < N) and rb[y + dc[k]][x + dr[k]] == 0 and paint[y + dc[k]][x + dr[k]] != 'B':
                                rb[y + dc[k]][x + dr[k]] = rb_num
                                rb_area.append([y + dc[k], x + dr[k]])
                                appended = 1
                    if appended == 0:
                        break

            if rgb[i][j] == 0:
                color = paint[i][j]
                rgb_num += 1
                rgb_area = [[i, j]]
                rgb[i][j] = rgb_num
                while True:
                    appended = 0
                    for y, x in rgb_area:
                        for k in range(4):
                            if (0 <= x + dr[k] < N and 0 <= y + dc[k] < N) and rgb[y + dc[k]][x + dr[k]] == 0 and paint[y + dc[k]][x + dr[k]] == color:
                                rgb[y + dc[k]][x + dr[k]] = rgb_num
                                rgb_area.append([y + dc[k], x + dr[k]])
                                appended = 1
                    if appended == 0:
                        break
        color = paint[i][j]

print(rgb_num, rb_num)