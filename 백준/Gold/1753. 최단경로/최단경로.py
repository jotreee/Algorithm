import sys
from heapq import heappop, heappush

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input().strip())
node = list([] for _ in range(V + 1))
for _ in range(E):
    u, v, w = map(int, input().split())
    node[u].append([v, w])

result = [3000001] * (V + 1)
result[K] = 0
heap = [[0, K]]

while True:
    cost, n = heappop(heap)
    for i, j in node[n]:
        if result[n] + j < result[i]:
            result[i] = result[n] + j
            heappush(heap, [result[i], i])
    if not heap:
        for i in range(V + 1):
            if result[i] == 3000001:
                result[i] = "INF"
        break

for i in range(1, V + 1):
    print(result[i])