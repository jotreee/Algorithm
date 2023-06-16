import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
campus = list(list(input().strip()) for _ in range(N))
visited = list(list([0] * M) for _ in range(N))
location = deque([])
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            location.append([i, j])
            visited[i][j] = 1
        elif campus[i][j] == 'X':
            visited[i][j] = 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

result = 0
while True:
    i, j = location.popleft()
    for k in range(4):
        if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M and not visited[i + dr[k]][j + dc[k]]:
            if campus[i + dr[k]][j + dc[k]] == 'P':
                result += 1
            visited[i + dr[k]][j + dc[k]] = 1
            location.append([i + dr[k], j + dc[k]])
    if not location:
        break

print(result if result else 'TT')