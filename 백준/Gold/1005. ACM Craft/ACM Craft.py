import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    seq = [[]] + list([D[i], [], []] for i in range(N))
    for _ in range(K):
        a, b = map(int, input().split())
        seq[a][2].append(b)
        seq[b][1].append(a)
    W = int(input().strip())
    nxt = deque([W])
    result = 0
    while True:
        n = nxt.popleft()
        if seq[n][1]:
            for m in seq[n][1]:
                if seq[m][0] < seq[n][0] + D[m - 1]:
                    seq[m][0] = seq[n][0] + D[m - 1]
                    nxt.append(m)
        else:
            if seq[n][0] > result:
                result = seq[n][0]
        if not nxt:
            print(result)
            break