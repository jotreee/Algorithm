import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    H, W, N = map(int, input().split())
    a = N % H
    if not a:
        a = H
    b = N // H
    if N > b * H:
        b += 1
    print(100 * a + b)