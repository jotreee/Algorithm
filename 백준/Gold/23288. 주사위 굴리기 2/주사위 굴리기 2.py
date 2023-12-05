import sys
from collections import deque

input = sys.stdin.readline


def move(n):
    global dice, D, x, y
    if n == 1:  # 동
        if y + 1 <= M - 1:
            y += 1
            dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
        else:
            D = 3
            y -= 1
            dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif n == 2:  # 남
        if x + 1 <= N - 1:
            x += 1
            dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
        else:
            D = 4
            x -= 1
            dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    elif n == 3:  # 서
        if y - 1 >= 0:
            y -= 1
            dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
        else:
            D = 1
            y += 1
            dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    else:  # 북
        if x - 1 >= 0:
            x -= 1
            dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
        else:
            D = 2
            x += 1
            dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]


N, M, K = map(int, input().split())
MAP = list(list(map(int, input().split())) for _ in range(N))
SUM = list(list([0] * M) for _ in range(N))

dice = [1, 2, 3, 4, 5, 6]
result = 0

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for x in range(N):
    for y in range(M):
        visited = list(list([0] * M) for _ in range(N))
        visited[x][y] = 1
        SUM[x][y] = MAP[x][y]
        same = deque([[x, y]])
        while True:
            i, j = same.popleft()
            for k in range(4):
                if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M and not visited[i + dr[k]][j + dc[k]] and MAP[i + dr[k]][j + dc[k]] == MAP[i][j]:
                    SUM[x][y] += MAP[i + dr[k]][j + dc[k]]
                    visited[i + dr[k]][j + dc[k]] = 1
                    same.append([i + dr[k], j + dc[k]])
            if not same:
                break

x, y = 0, 0
D = 1

for _ in range(K):
    move(D)
    result += SUM[x][y]

    A, B = dice[5], MAP[x][y]
    if A > B:
        D += (1 if D < 4 else -3)
    elif A < B:
        D += (-1 if D > 1 else 3)

print(result)