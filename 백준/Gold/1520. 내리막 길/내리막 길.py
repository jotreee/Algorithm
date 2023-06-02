import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
MAP = list(list(map(int, input().split())) for _ in range(M))
dp = list(list([0] * N) for _ in range(M))
decided = list(list([0] * N) for _ in range(M))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(M):
    for j in range(N):
        if MAP[i][j] >= MAP[0][0]:
            decided[i][j] = 1
        else:
            for k in range(4):
                if 0 <= i + dr[k] < M and 0 <= j + dc[k] < N and MAP[i + dr[k]][j + dc[k]] > MAP[i][j]:
                    break
            else:
                decided[i][j] = 1
dp[0][0] = 1

while True:
    changed = 0
    for i in range(M):
        for j in range(N):
            if not decided[i][j]:
                changed = 1
                for k in range(4):
                    if 0 <= i + dr[k] < M and 0 <= j + dc[k] < N and MAP[i + dr[k]][j + dc[k]] > MAP[i][j]:
                        if decided[i + dr[k]][j + dc[k]]:
                            decided[i][j] = 1
                            dp[i][j] += dp[i + dr[k]][j + dc[k]]
                        else:
                            decided[i][j] = 0
                            dp[i][j] = 0
                            break

    if not changed:
        print(dp[-1][-1])
        break