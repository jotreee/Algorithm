import sys

input = sys.stdin.readline


def heap_in(n):
    global heap
    heap.append(n)
    idx = len(heap) - 1

    while True:
        if idx == 1:
            break
        elif idx % 2 and heap[idx] > heap[(idx - 1) // 2]:
            heap[idx], heap[(idx - 1) // 2] = heap[(idx - 1) // 2], heap[idx]
            idx = (idx - 1) // 2
        elif not idx % 2 and heap[idx] > heap[idx // 2]:
            heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
            idx //= 2
        else:
            break


def heap_out():
    global heap
    print(heap[1])
    heap[1], heap[-1] = heap[-1], heap[1]
    heap.pop()
    idx = 1

    while True:
        if 2 * idx + 1 < len(heap) and heap[idx] < heap[2 * idx + 1] and heap[2 * idx] < heap[2 * idx + 1]:
            heap[idx], heap[2 * idx + 1] = heap[2 * idx + 1], heap[idx]
            idx = 2 * idx + 1
        elif 2 * idx < len(heap) and heap[idx] < heap[2 * idx]:
            heap[idx], heap[2 * idx] = heap[2 * idx], heap[idx]
            idx *= 2
        else:
            break


N = int(input().strip())
heap = [0]

for _ in range(N):
    n = int(input().strip())
    if n:
        heap_in(n)
    else:
        if len(heap) == 1:
            print(0)
        else:
            heap_out()