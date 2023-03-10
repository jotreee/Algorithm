import sys

input = sys.stdin.readline


def dfs(i, j, y, x, cnt, s, visited):
    global result
    if not cnt:
        if s > result:
            result = s
        return

    for k in range(4):
        if 0 <= y + dr[k] < N and 0 <= x + dc[k] < M and not visited[y + dr[k] - i][x + dc[k] - j]:
            visited[y + dr[k] - i][x + dc[k] - j] = 1
            dfs(i, j, y + dr[k], x + dc[k], cnt - 1, s + paper[y + dr[k]][x + dc[k]], visited)
            visited[y + dr[k] - i][x + dc[k] - j] = 0


N, M = map(int, input().split())
paper = list(list(map(int, input().split())) for _ in range(N))

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

result = 0
for i in range(N):
    for j in range(M):
        visit = list([0] * 7 for _ in range(7))
        visit[0][0] = 1
        dfs(i, j, i, j, 3, paper[i][j], visit)

for i in range(N - 1):
    for j in range(M - 2):
        num = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j + 1]
        if num > result:
            result = num
        num = paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 1][j + 2] + paper[i][j + 1]
        if num > result:
            result = num

for i in range(N - 2):
    for j in range(M - 1):
        num = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 1][j + 1]
        if num > result:
            result = num
        num = paper[i][j + 1] + paper[i + 1][j + 1] + paper[i + 2][j + 1] + paper[i + 1][j]
        if num > result:
            result = num

print(result)
