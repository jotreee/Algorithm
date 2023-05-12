import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
paper = list(list(map(int, input().split())) for _ in range(N))
paper[0][0] = -1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

air = deque([[0, 0]])
while True:
    i, j = air.popleft()
    for k in range(4):
        if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M and not paper[i + dr[k]][j + dc[k]]:
            paper[i + dr[k]][j + dc[k]] = -1
            air.append([i + dr[k], j + dc[k]])

    if not air:
        break

hour = 0
while True:
    hour += 1
    melted = deque()
    cheese = 0
    for i in range(N):
        for j in range(M):
            if paper[i][j] > 0:
                cheese = 1
                air = 0
                for k in range(4):
                    if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M and paper[i + dr[k]][j + dc[k]] == -1:
                        air += 1
                if air >= 2:
                    paper[i][j] -= 1
                    if not paper[i][j]:
                        melted.append([i, j])

    if melted:
        for i, j in melted:
            paper[i][j] = -1
        while True:
            i, j = melted.popleft()
            for k in range(4):
                if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M and not paper[i + dr[k]][j + dc[k]]:
                    paper[i + dr[k]][j + dc[k]] = -1
                    melted.append([i + dr[k], j + dc[k]])
            if not melted:
                break

    if not cheese:
        print(hour - 1)
        break