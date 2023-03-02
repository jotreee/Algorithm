import sys, copy
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
house = list(list(map(int, input().strip())) for _ in range(N))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

result = []
for i in range(N):
    for j in range(N):
        if house[i][j]:
            num = 1
            house[i][j] = 0
            group = deque()
            group.append([i, j])
            while True:
                for y, x in copy.deepcopy(group):
                    for k in range(4):
                        if 0 <= y + dr[k] < N and 0 <= x + dc[k] < N and house[y + dr[k]][x + dc[k]]:
                            group.append([y + dr[k], x + dc[k]])
                            house[y + dr[k]][x + dc[k]] -= 1
                            num += 1
                    group.popleft()
                if not group:
                    result.append(num)
                    break

result.sort()
print(len(result))
for i in result:
    print(i)