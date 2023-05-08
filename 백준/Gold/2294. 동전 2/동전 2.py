import sys

input = sys.stdin.readline

n, k = map(int, input().split())
cost = [1000001] * (k + 1)
for _ in range(n):
    coin = int(input().strip())
    if coin <= k:
        cost[coin] = 1
        for i in range(coin + 1, k + 1):
            if not i % coin and i // coin < cost[i]:
                cost[i] = i // coin
            if cost[i - coin] + 1 < cost[i]:
                cost[i] = cost[i - coin] + 1

if cost[k] == 1000001:
    print(-1)
else:
    print(cost[k])