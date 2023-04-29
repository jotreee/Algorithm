import sys

input = sys.stdin.readline

N = int(input().strip())
P = list(map(int, input().split()))
cost = [0] * N
cost[0] = P[0]

for i in range(1, N):
    nxt = [P[i]]
    for j in range(i if i % 2 else i - 1):
        nxt.append(cost[i - 1 - j] + cost[j])
    cost[i] = max(nxt)

print(cost[N - 1])