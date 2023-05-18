import sys, copy

input = sys.stdin.readline

N = int(input().strip())
house = list(list(map(int, input().split())) for _ in range(N))

result = 1000 * N
dp = copy.deepcopy(house)
dp[0][1], dp[0][2] = 1001, 1001
for i in range(1, N):
    dp[i][0] += (dp[i - 1][1] if dp[i - 1][1] <= dp[i - 1][2] else dp[i - 1][2])
    dp[i][1] += (dp[i - 1][0] if dp[i - 1][0] <= dp[i - 1][2] else dp[i - 1][2])
    dp[i][2] += (dp[i - 1][0] if dp[i - 1][0] <= dp[i - 1][1] else dp[i - 1][1])
if dp[-1][1] < result or dp[-1][2] < result:
    result = (dp[-1][1] if dp[-1][1] <= dp[-1][2] else dp[-1][2])

dp = copy.deepcopy(house)
dp[0][0], dp[0][2] = 1001, 1001
for i in range(1, N):
    dp[i][0] += (dp[i - 1][1] if dp[i - 1][1] <= dp[i - 1][2] else dp[i - 1][2])
    dp[i][1] += (dp[i - 1][0] if dp[i - 1][0] <= dp[i - 1][2] else dp[i - 1][2])
    dp[i][2] += (dp[i - 1][0] if dp[i - 1][0] <= dp[i - 1][1] else dp[i - 1][1])
if dp[-1][0] < result or dp[-1][2] < result:
    result = (dp[-1][0] if dp[-1][0] <= dp[-1][2] else dp[-1][2])

dp = copy.deepcopy(house)
dp[0][0], dp[0][1] = 1001, 1001
for i in range(1, N):
    dp[i][0] += (dp[i - 1][1] if dp[i - 1][1] <= dp[i - 1][2] else dp[i - 1][2])
    dp[i][1] += (dp[i - 1][0] if dp[i - 1][0] <= dp[i - 1][2] else dp[i - 1][2])
    dp[i][2] += (dp[i - 1][0] if dp[i - 1][0] <= dp[i - 1][1] else dp[i - 1][1])
if dp[-1][0] < result or dp[-1][1] < result:
    result = (dp[-1][0] if dp[-1][0] <= dp[-1][1] else dp[-1][1])

print(result)