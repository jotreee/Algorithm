import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
station = list([] for _ in range(n + 1))
for _ in range(m):
    bus = list(map(int, input().split()))
    station[bus[0]].append([bus[1], bus[2]])
start, end = map(int, input().split())

heap = [[0, start]]
result = list([100000000, []] for _ in range(n + 1))
result[start] = [0, [start]]

while True:
    cost, n = heappop(heap)
    if n == end:
        print(cost)
        print(len(result[end][1]))
        print(" ".join(map(str, result[end][1])))
        break
    for i, j in station[n]:
        if result[i][0] > result[n][0] + j:
            result[i] = [result[n][0] + j, result[n][1] + [i]]
            heappush(heap, [result[i][0], i])