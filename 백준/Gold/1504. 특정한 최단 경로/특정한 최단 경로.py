import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, E = map(int, input().split())
node = list([] for _ in range(N + 1))
for _ in range(E):
    a, b, c = map(int, input().split())
    node[a].append([b, c])
    node[b].append([a, c])
u, v = map(int, input().split())

start = [160000000001] * (N + 1)
start[1] = 0
heap = [[0, 1]]
while True:
    l, n = heappop(heap)
    for i, j in node[n]:
        if start[n] + j < start[i]:
            start[i] = start[n] + j
            heappush(heap, [start[i], i])
    if not heap:
        break

U = [160000000001] * (N + 1)
U[u] = 0
heap = [[0, u]]
while True:
    l, n = heappop(heap)
    for i, j in node[n]:
        if U[n] + j < U[i]:
            U[i] = U[n] + j
            heappush(heap, [U[i], i])
    if not heap:
        break

V = [160000000001] * (N + 1)
V[v] = 0
heap = [[0, v]]
while True:
    l, n = heappop(heap)
    for i, j in node[n]:
        if V[n] + j < V[i]:
            V[i] = V[n] + j
            heappush(heap, [V[i], i])
    if not heap:
        break

result = min(160000000001, start[v] + V[u] + U[N], start[u] + U[v] + V[N])
if result == 160000000001:
    print(-1)
else:
    print(result)