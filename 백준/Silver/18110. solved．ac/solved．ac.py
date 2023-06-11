import sys

input = sys.stdin.readline


def r(n):
    if n % 1 < 0.5:
        return int(n // 1)
    else:
        return int(n // 1) + 1


N = int(input().strip())
if not N:
    print(0)
elif N == 1:
    print(input().strip())
else:
    n = r(N * 0.15)
    arr = list(int(input().strip()) for _ in range(N))
    arr.sort()
    print(r(sum(arr[n:N - n]) / (N - 2 * n)))