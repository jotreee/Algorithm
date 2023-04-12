import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
land = []
for _ in range(N):
    land += list(map(int, input().split()))
land.sort()

result = [128000000, 250000]
for h in range(land[0], min(((B + sum(land)) // len(land)), 256) + 1):
    t = 0
    for n in land:
        if n < h:
            t += h - n
        elif n > h:
            t += 2 * (n - h)
    if t <= result[0]:
        result = [t, h]

print(" ".join(map(str, result)))