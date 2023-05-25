import sys

input = sys.stdin.readline

N, M = map(int, input().split())
cost = list(list(map(int, input().split())) for _ in range(2))

result = 10001
dp = list([0] * (sum(cost[1]) + 1) for _ in range(N + 1))
for i in range(1, N + 1):
    for j in range(1, sum(cost[1]) + 1):
        dp[i][j] = (dp[i][j - 1] if dp[i][j - 1] > dp[i - 1][j] else dp[i - 1][j])
        if j >= cost[1][i - 1] and dp[i - 1][j - cost[1][i - 1]] + cost[0][i - 1] > dp[i][j]:
            dp[i][j] = dp[i - 1][j - cost[1][i - 1]] + cost[0][i - 1]
        if M <= dp[i][j] and j < result:
            result = j

print(result)