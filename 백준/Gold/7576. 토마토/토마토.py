import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = deque(deque(map(int, input().split())) for _ in range(N))

ripen = 1
ripe = deque()
for i in range(N):
    for j in range(M):
        if ripen == 1 and tomato[i][j] == 0:
            ripen = 0
        if tomato[i][j] == 1:
            ripe.append([i, j])

if ripen == 1:
    print(0)

else:
    day = 0
    while True:
        new = deque()
        for i, j in ripe:
            if i > 0 and tomato[i - 1][j] == 0:
                tomato[i - 1][j] = 1
                new.append([i - 1, j])
            if i < N - 1 and tomato[i + 1][j] == 0:
                tomato[i + 1][j] = 1
                new.append([i + 1, j])
            if j > 0 and tomato[i][j - 1] == 0:
                tomato[i][j - 1] = 1
                new.append([i, j - 1])
            if j < M - 1 and tomato[i][j + 1] == 0:
                tomato[i][j + 1] = 1
                new.append([i, j + 1])

        if new:
            day += 1
            ripe = deepcopy(new)

        else:
            not_ripe = 0
            for i in range(N):
                for j in range(M):
                    if tomato[i][j] == 0:
                        not_ripe = 1
                        print(-1)
                        break
                if not_ripe == 1:
                    break
            else:
                print(day)
            break