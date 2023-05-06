import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, input().split())
    if W <= K:
        for i in range(K, W, -1):
            if dp[i - W] and dp[i] < dp[i - W] + V:
                dp[i] = dp[i - W] + V
        if dp[W] < V:
            dp[W] = V

print(max(dp))