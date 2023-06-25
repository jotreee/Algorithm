import sys
from collections import deque

input = sys.stdin.readline

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    building = []
    for _ in range(L):
        building.append(list(list(input().strip()) for _ in range(R)))
        n = input().strip()
    found = 0
    move = deque([])
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    move = deque([[i, j, k]])
                    building[i][j][k] = 0
                    found = 1
                    break
            if found:
                break
        if found:
            break

    dl = [0, 0, 1, -1, 0, 0]
    dr = [0, 0, 0, 0, 1, -1]
    dc = [1, -1, 0, 0, 0, 0]


    while True:
        i, j, k = move.popleft()
        found = 0
        for d in range(6):
            if 0 <= i + dl[d] < L and 0 <= j + dr[d] < R and 0 <= k + dc[d] < C:
                if building[i + dl[d]][j + dr[d]][k + dc[d]] == 'E':
                    found = 1
                    print(f'Escaped in {building[i][j][k] + 1} minute(s).')
                    break
                elif building[i + dl[d]][j + dr[d]][k + dc[d]] == '.':
                    building[i + dl[d]][j + dr[d]][k + dc[d]] = building[i][j][k] + 1
                    move.append([i + dl[d], j + dr[d], k + dc[d]])
        if found:
            break
        if not move:
            print('Trapped!')
            break