import sys

input = sys.stdin.readline

N = int(input().strip())
sea = list(list(map(int, input().split())) for _ in range(N))
shark = [0, 0, 2, 0]
find = 0
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark[0], shark[1] = i, j
            sea[i][j] = 0
            find = 1
            break
    if find:
        break

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

time = 0
help = 0
while True:
    loc = [[shark[0], shark[1]]]
    visited = list([0] * N for _ in range(N))
    visited[shark[0]][shark[1]] = 1
    distance = 1
    n = 0
    while True:
        n += 1
        if n == N * N:
            help = 1
            break
        fish = []
        nxt = []
        for i, j in loc:
            for k in range(4):
                if 0 <= i + dr[k] < N and 0 <= j + dc[k] < N and not visited[i + dr[k]][j + dc[k]] and sea[i + dr[k]][j + dc[k]] <= shark[2]:
                    visited[i + dr[k]][j + dc[k]] = 1
                    nxt.append([i + dr[k], j + dc[k]])
                    if 0 < sea[i + dr[k]][j + dc[k]] < shark[2]:
                        fish.append([i + dr[k], j + dc[k]])
        if fish:
            fish.sort()
            sea[fish[0][0]][fish[0][1]] = 0
            shark[0], shark[1] = fish[0][0], fish[0][1]
            shark[3] += 1
            if shark[2] == shark[3]:
                shark[2] += 1
                shark[3] = 0
            time += distance
            break
        else:
            loc = nxt
            distance += 1
    if help:
        break

print(time)