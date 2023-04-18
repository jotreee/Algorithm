import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
station = list([] for _ in range(N + 1))
for _ in range(M):
    bus = list(map(int, input().split()))
    station[bus[0]].append([bus[1], bus[2]])
start, end = map(int, input().split())

if start == end:
    print(0)

else:
    node = [100000000] * (N + 1)
    node[start] = 0
    heap = [[0, start]]
    while True:
        cost, n = heappop(heap)
        if n == end:
            print(cost)
            break
        for i, j in station[n]:
            if node[n] + j < node[i]:
                node[i] = node[n] + j
                heappush(heap, [node[i], i])