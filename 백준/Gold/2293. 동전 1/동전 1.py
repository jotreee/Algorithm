import sys

input = sys.stdin.readline

n, k = map(int, input().split())
cost = [0] * (k + 1)
for _ in range(n):
    coin = int(input().strip())
    if coin <= k:
        cost[coin] += 1
        for i in range(coin + 1, k + 1):
            cost[i] += cost[i - coin]

print(cost[k])