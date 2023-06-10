import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
MAP = list(list(map(int, input().split())) for _ in range(N))
distance = list(list([-1] * M) for _ in range(N))
nxt = deque([])
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 2:
            distance[y][x] = 0
            nxt.append([y, x])
        if not MAP[y][x]:
            distance[y][x] = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
while True:
    i, j = nxt.popleft()
    for k in range(4):
        if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M and distance[i + dr[k]][j + dc[k]] == -1:
            distance[i + dr[k]][j + dc[k]] = distance[i][j] + 1
            nxt.append([i + dr[k], j + dc[k]])
    if not nxt:
        for n in range(N):
            print(" ".join(map(str, distance[n])))
        break