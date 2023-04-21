import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
world = list(list(map(int, input().split())) for _ in range(N))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

day = 0
while True:
    visited = list([0] * N for _ in range(N))
    people = list([0, 0] for _ in range(N * N + 1))
    n = 0
    change = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and ((i + 1 < N and L <= abs(world[i][j] - world[i + 1][j]) <= R) or (j + 1 < N and L <= abs(world[i][j] - world[i][j + 1]) <= R)):
                change = 1
                union = deque([[i, j]])
                n += 1
                people[n] = [world[i][j], 1]
                visited[i][j] = n
                while True:
                    y, x = union[0]
                    for k in range(4):
                        if 0 <= x + dr[k] < N and 0 <= y + dc[k] < N and not visited[y + dc[k]][x + dr[k]] and L <= abs(world[y][x] - world[y + dc[k]][x + dr[k]]) <= R:
                            union.append([y + dc[k], x + dr[k]])
                            people[n][0] += world[y + dc[k]][x + dr[k]]
                            people[n][1] += 1
                            visited[y + dc[k]][x + dr[k]] = n
                    union.popleft()
                    if not union:
                        break
    if not change:
        break
    else:
        day += 1
        for i in range(N):
            for j in range(N):
                if visited[i][j]:
                    world[i][j] = people[visited[i][j]][0] // people[visited[i][j]][1]

print(day)