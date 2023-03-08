import sys, heapq

input = sys.stdin.readline

N = int(input().strip())
heap = []
for _ in range(N):
    n = int(input().strip())
    if not n:
        if heap:
            a, b = heapq.heappop(heap)
            print(a * b)
        else:
            print(0)
    elif n < 0:
        heapq.heappush(heap, [-n, -1])
    else:
        heapq.heappush(heap, [n, 1])