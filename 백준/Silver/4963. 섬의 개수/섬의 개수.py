import sys, copy
from collections import deque

input = sys.stdin.readline

dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    Map = list(list(map(int, input().split())) for _ in range(h))
    visited = list([0] * w for _ in range(h))

    land = 0
    for i in range(h):
        for j in range(w):
            if Map[i][j] and not visited[i][j]:
                land += 1
                visited[i][j] = 1
                ground = deque([[i, j]])
                while True:
                    for y, x in copy.deepcopy(ground):
                        for k in range(8):
                            if 0 <= x + dc[k] < w and 0 <= y + dr[k] < h and Map[y + dr[k]][x + dc[k]] and not visited[y + dr[k]][x + dc[k]]:
                                visited[y + dr[k]][x + dc[k]] = 1
                                ground.append([y + dr[k], x + dc[k]])
                        ground.popleft()
                    if not ground:
                        break

    print(land)