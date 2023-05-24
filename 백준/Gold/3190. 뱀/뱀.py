import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())
board = list([0] * N for _ in range(N))
snake = deque([[0, 0]])
board[0][0] = -1
for _ in range(K):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1

L = int(input().strip())
rotate = list([] for _ in range(10102))
for _ in range(L):
    a, b = input().split()
    rotate[int(a) + 1] = b

result = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0
for n in range(1, 10102):
    if rotate[n] == 'L':
        d -= 1
        if d < 0:
            d += 4
    elif rotate[n] == 'D':
        d += 1
        if d > 3:
            d -= 4

    i, j = snake[0][0], snake[0][1]
    if (i + dr[d] < 0) or (i + dr[d] >= N) or (j + dc[d] < 0) or (j + dc[d] >= N):
        print(n)
        break

    elif board[i + dr[d]][j + dc[d]] == -1:
        print(n)
        break

    elif not board[i + dr[d]][j + dc[d]]:
        board[i + dr[d]][j + dc[d]] = -1
        snake.appendleft([i + dr[d], j + dc[d]])
        board[snake[-1][0]][snake[-1][1]] = 0
        snake.pop()

    elif board[i + dr[d]][j + dc[d]] == 1:
        board[i + dr[d]][j + dc[d]] = -1
        snake.appendleft([i + dr[d], j + dc[d]])