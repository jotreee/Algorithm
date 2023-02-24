import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin = list(int(input().strip()) for _ in range(N))
num = 0

for i in range(N - 1, -1, -1):
    if coin[i] <= K:
        num += K // coin[i]
        K %= coin[i]

    if K == 0:
        break

print(num)