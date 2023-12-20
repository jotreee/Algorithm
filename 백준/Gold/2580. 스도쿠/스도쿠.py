import sys
from collections import deque

input = sys.stdin.readline

sudoku = list(list(map(int, input().split())) for _ in range(9))
empty = []
for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            empty.append([i, j])

idx = 0
fill = []
while True:
    fill.append(deque())
    nums = [0] * 10
    for n in range(9):
        nums[sudoku[empty[idx][0]][n]] += 1
        nums[sudoku[n][empty[idx][1]]] += 1
    for i in range(3):
        for j in range(3):
            nums[sudoku[3 * (empty[idx][0] // 3) + i][3 * (empty[idx][1] // 3) + j]] += 1
    for n in range(1, 10):
        if not nums[n]:
            fill[-1].append(n)

    while True:
        if not fill[-1]:
            fill.pop()
            idx -= 1
            sudoku[empty[idx][0]][empty[idx][1]] = 0
        else:
            sudoku[empty[idx][0]][empty[idx][1]] = fill[-1].popleft()
            idx += 1
            break

    if idx == len(empty):
        for n in range(9):
            print(" ".join(map(str, sudoku[n])))
        break