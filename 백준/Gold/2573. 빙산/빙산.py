import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ice = list(list(map(int, input().split())) for _ in range(N))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

year = 0
while True:
    year += 1
    nxt = list([0] * M for _ in range(N))
    melted = 0
    for i in range(N):
        for j in range(M):
            if ice[i][j]:
                nxt[i][j] = ice[i][j]
                for k in range(4):
                    if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M and not ice[i + dr[k]][j + dc[k]]:
                        nxt[i][j] -= 1
                if nxt[i][j] < 0:
                    nxt[i][j] = 0
                if not nxt[i][j] and not melted:
                    melted = 1

    if melted:
        area = 0
        sea = list([0] * M for _ in range(N))
        for i in range(N):
            for j in range(M):
                if nxt[i][j] and not sea[i][j]:
                    area += 1
                    sea[i][j] = area
                    connected = deque([[i, j]])
                    while True:
                        y, x = connected.popleft()
                        for k in range(4):
                            if 0 <= y + dr[k] < N and 0 <= x + dc[k] < M and nxt[y + dr[k]][x + dc[k]] and not sea[y + dr[k]][x + dc[k]]:
                                sea[y + dr[k]][x + dc[k]] = area
                                connected.append([y + dr[k], x + dc[k]])

                        if not connected:
                            break
        if not area:
            print(0)
            break
        elif area > 1:
            print(year)
            break

    ice = nxt