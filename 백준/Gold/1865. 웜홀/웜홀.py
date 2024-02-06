import sys
from collections import deque

input = sys.stdin.readline

TC = int(input().strip())
for _ in range(TC):
    N, M, W = map(int, input().split())  # 지점, 도로, 웜홀
    spot = list([] for _ in range(N + 1))
    for _ in range(M):
        S, E, T = map(int, input().split())
        spot[S].append([E, T])
        spot[E].append([S, T])
    for _ in range(W):
        S, E, T = map(int, input().split())
        spot[S].append([E, -T])

    for i in range(1, N + 1):
        time = [M * 10000] * (N + 1)
        time[i] = 0
        nxt = deque([i])
        while True:
            n = nxt.popleft()
            for a, b in spot[n]:
                if time[n] > -M * 10000 and time[n] + b < time[a]:
                    time[a] = time[n] + b
                    nxt.append(a)
            if not nxt or time[i] < 0:
                break

        if time[i] < 0:
            print("YES")
            break

    else:
        print("NO")
