import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
forest = list(list(input().strip()) for _ in range(R))
hedgehog = deque([])
water = deque([])
for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':
            hedgehog.append([i, j])
        elif forest[i][j] == '*':
            water.append([i, j])

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
time = 0
while True:
    time += 1
    if water:
        nxt_water = deque([])
        while True:
            i, j = water.popleft()
            for k in range(4):
                if 0 <= i + dr[k] < R and 0 <= j + dc[k] < C and (forest[i + dr[k]][j + dc[k]] == '.' or forest[i + dr[k]][j + dc[k]] == 'S'):
                    forest[i + dr[k]][j + dc[k]] = '*'
                    nxt_water.append([i + dr[k], j + dc[k]])
            if not water:
                water = nxt_water
                break

    found = 0
    if hedgehog:
        nxt_hedgehog = deque([])
        found = 0
        while True:
            i, j = hedgehog.popleft()
            for k in range(4):
                if 0 <= i + dr[k] < R and 0 <= j + dc[k] < C:
                    if forest[i + dr[k]][j + dc[k]] == 'D':
                        found = 1
                        break
                    if forest[i + dr[k]][j + dc[k]] == '.':
                        forest[i + dr[k]][j + dc[k]] = 'S'
                        nxt_hedgehog.append([i + dr[k], j + dc[k]])
            if not hedgehog:
                hedgehog = nxt_hedgehog
                break
        if found:
            print(time)
            break

        if not hedgehog:
            print('KAKTUS')
            break