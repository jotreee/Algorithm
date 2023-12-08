import sys

input = sys.stdin.readline


def group(n):
    global nums
    while True:
        if n == nums[n]:
            return n
        else:
            n = nums[n]


N, M = map(int, input().split())
nums = list(i for i in range(N + 1))
for _ in range(M):
    x, y, z = map(int, input().split())
    if x:
        print("YES" if y == z or group(y) == group(z) else "NO")
    else:
        a, b = group(y), group(z)
        nums[a], nums[b] = min(a, b), min(a, b)