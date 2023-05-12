import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
bus = list([] for _ in range(N + 1))
for _ in range(M):
    a, b, c = map(int, input().split())
    bus[a].append([b, c])

for k in range(1, N + 1):
    result = [10000000001] * (N + 1)
    result[k] = 0
    heap = [[0, k]]

    while True:
        cost, n = heappop(heap)
        for i, j in bus[n]:
            if result[i] > result[n] + j:
                result[i] = result[n] + j
                heappush(heap, [result[i], i])

        if not heap:
            for i in range(N + 1):
                if result[i] == 10000000001:
                    result[i] = 0
            break

    print(" ".join(map(str, result[1:])))