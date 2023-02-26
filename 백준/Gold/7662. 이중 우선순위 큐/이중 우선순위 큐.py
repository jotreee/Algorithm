import sys, heapq
from collections import deque

input = sys.stdin.readline

T = int(input().strip())
for tc in range(T):
    N = int(input().strip())

    nums = [0] * N
    min_heap = []
    max_heap = []

    for i in range(N):
        order = list(input().split())
        if order[0] == 'I':
            heapq.heappush(min_heap, [int(order[1]), i])
            heapq.heappush(max_heap, [-int(order[1]), i])
            nums[i] = 1
        else:
            if order[1] == '1':
                while True:
                    if not max_heap:
                        break
                    out = heapq.heappop(max_heap)[1]
                    if nums[out] > 0:
                        nums[out] = 0
                        break
            else:
                while True:
                    if not min_heap:
                        break
                    out = heapq.heappop(min_heap)[1]
                    if nums[out] > 0:
                        nums[out] -= 1
                        break

    result_min, result_max = 0, 0
    while True:
        if not max_heap:
            break
        if nums[max_heap[0][1]] > 0:
            result_max = -max_heap[0][0]
            break
        else:
            heapq.heappop(max_heap)

    while True:
        if not min_heap:
            break
        if nums[min_heap[0][1]] > 0:
            result_min = min_heap[0][0]
            break
        else:
            heapq.heappop(min_heap)

    if not max_heap:
        print("EMPTY")
    else:
        print(result_max, result_min)