import sys

input = sys.stdin.readline

N = int(input().strip())
room = list(list(map(int, input().split())) for _ in range(N))

dp = list(list([0, 0, 0] for _ in range(N)) for _ in range(N))
for i in range(1, N):
    if not room[0][i]:
        dp[0][i][0] = 1
    else:
        break

for i in range(1, N):
    for j in range(2, N):
        if not room[i][j]:
            if not room[i][j - 1]:
                dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]
            if not room[i - 1][j - 1] and not room[i - 1][j] and not room[i][j - 1]:
                dp[i][j][1] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
            if not room[i - 1][j]:
                dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]

print(sum(dp[N - 1][N - 1]))