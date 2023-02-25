import sys

input = sys.stdin.readline

N, M = map(int, input().split())
maze = list(list(map(int, input().strip())) for _ in range(N))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

maze[0][0] = 2
num = 2
nxt = [[0, 0]]

while True:
    end = 0
    num += 1
    new = []
    for i, j in nxt:
        for k in range(4):
            if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M and maze[i + dr[k]][j + dc[k]] == 1:
                if i + dr[k] == N - 1 and j + dc[k] == M - 1:
                    print(num - 1)
                    end = 1
                    break
                maze[i + dr[k]][j + dc[k]] = num
                new.append([i + dr[k], j + dc[k]])
        if end == 1:
            break
    if end == 1:
        break
    else:
        nxt = new