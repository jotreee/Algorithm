import sys, copy

input = sys.stdin.readline

N, M = map(int, input().split())
spots = [0] * N
connected = list(list(i for i in range(N + 1)) for _ in range(2))

cnt = 0
result = 0
for i in range(1, M + 1):
    a, b = map(int, input().split())
    if not spots[a] and not spots[b]:
        cnt += 1
        spots[a], spots[b] = cnt, cnt

    elif not spots[a] and spots[b]:
        spots[a] = spots[b]

    elif spots[a] and not spots[b]:
        spots[b] = spots[a]

    else:
        n, m = spots[a], spots[b]
        while True:
            if connected[0][n] != connected[1][n]:
                n = connected[1][n]
            else:
                break
        while True:
            if connected[0][m] != connected[1][m]:
                m = connected[1][m]
            else:
                break

        if n != m:
            connected[1][m] = connected[1][n]
        else:
            result = i
            break

print(result)