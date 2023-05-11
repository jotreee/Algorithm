import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    coins = list(map(int, input().split()))
    M = int(input().strip())
    cost = [0] * (M + 1)
    for c in coins:
        if c <= M:
            cost[c] += 1
            for i in range(c + 1, M + 1):
                cost[i] += cost[i - c]
                
    print(cost[M])