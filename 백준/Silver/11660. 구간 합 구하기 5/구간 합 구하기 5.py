import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(N))

for i in range(N):
    for j in range(N - 1):
        graph[i][j + 1] += graph[i][j]
for i in range(N - 1):
    for j in range(N):
        graph[i + 1][j] += graph[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == y1 == 1:
        print(graph[x2 - 1][y2 - 1])
    elif x1 == 1:
        print(graph[x2 - 1][y2 - 1] - graph[x2 - 1][y1 - 2])
    elif y1 == 1:
        print(graph[x2 - 1][y2 - 1] - graph[x1 - 2][y2 - 1])
    else:
        print(graph[x2 - 1][y2 - 1] - graph[x2 - 1][y1 - 2] - graph[x1 - 2][y2 - 1] + graph[x1 - 2][y1 - 2])