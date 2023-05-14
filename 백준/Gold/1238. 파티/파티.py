import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M, X = map(int, input().split())
way = list([] for _ in range(N + 1))
go = [1000000001] * (N + 1)
back = [1000000001] * (N + 1)
for _ in range(M):
    s, e, t = map(int, input().split())
    way[s].append([e, t])

# go
for n in range(1, N + 1):
    home = [1000000001] * (N + 1)
    home[n] = 0
    heap = [[0, n]]
    while True:
        time, city = heappop(heap)
        if city == X:
            go[n] = time
            break
        for i, j in way[city]:
            if home[city] + j < home[i]:
                home[i] = home[city] + j
                heappush(heap, [home[i], i])

# back
heap = [[0, X]]
back[X] = 0
while True:
    time, city = heappop(heap)
    for i, j in way[city]:
        if back[city] + j < back[i]:
            back[i] = back[city] + j
            heappush(heap, [back[i], i])
    if not heap:
        break

result = 0
for n in range(1, N + 1):
    if go[n] + back[n] > result:
        result = go[n] + back[n]

print(result)