import sys
from collections import deque

input = sys.stdin.readline

sudoku = list(list(map(int, input().strip())) for _ in range(9))
empty = []
for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            empty.append([i, j, deque()])

n, go = 0, 1
while True:
    if n >= len(empty):
        for i in range(9):
            print("".join(map(str, sudoku[i])))
        break

    if go:
        number = [0] * 10
        for i in range(9):
            number[sudoku[empty[n][0]][i]] = 1
            number[sudoku[i][empty[n][1]]] = 1
        for i in range(3):
            for j in range(3):
                number[sudoku[(empty[n][0] // 3) * 3 + i][(empty[n][1] // 3) * 3 + j]] = 1
        for i in range(1, 10):
            if not number[i]:
                empty[n][2].append(i)
        if not empty[n][2]:
            go = 0
            n -= 1
        else:
            sudoku[empty[n][0]][empty[n][1]] = empty[n][2].popleft()
            n += 1

    else:
        if not empty[n][2]:
            sudoku[empty[n][0]][empty[n][1]] = 0
            n -= 1
        else:
            sudoku[empty[n][0]][empty[n][1]] = empty[n][2].popleft()
            go = 1
            n += 1