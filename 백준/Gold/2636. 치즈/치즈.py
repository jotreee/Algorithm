import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

air = deque([[0, 0]])
board[0][0] = -1
while True:
    i, j = air.popleft()
    for k in range(4):
        if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M and not board[i + dr[k]][j + dc[k]]:
            board[i + dr[k]][j + dc[k]] = -1
            air.append([i + dr[k], j + dc[k]])
    if not air:
        break

melt = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            for k in range(4):
                if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M and board[i + dr[k]][j + dc[k]] == -1:
                    board[i][j] = 2
                    melt.append([i, j])
                    break

time = 0
cheese = 0
while True:
    if melt:
        nxt = []
        time += 1
        cheese = len(melt)
        for i, j in melt:
            board[i][j] = -1
            for k in range(4):
                if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M:
                    if board[i + dr[k]][j + dc[k]] == 1:
                        board[i + dr[k]][j + dc[k]] = 2
                        nxt.append([i + dr[k], j + dc[k]])
                    if not board[i + dr[k]][j + dc[k]]:
                        air = deque([[i + dr[k], j + dc[k]]])
                        board[i + dr[k]][j + dc[k]] = -1
                        while True:
                            y, x = air.popleft()
                            for z in range(4):
                                if 0 <= y + dr[z] < N and 0 <= x + dc[z] < M:
                                    if board[y + dr[z]][x + dc[z]] == 1:
                                        board[y + dr[z]][x + dc[z]] = 2
                                        nxt.append([y + dr[z], x + dc[z]])
                                    elif not board[y + dr[z]][x + dc[z]]:
                                        board[y + dr[z]][x + dc[z]] = -1
                                        air.append([y + dr[z], x + dc[z]])
                            if not air:
                                break
        melt = nxt
        
    else:
        print(time)
        print(cheese)
        break