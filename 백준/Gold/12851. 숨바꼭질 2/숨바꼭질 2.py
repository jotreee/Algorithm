import sys
sys.setrecursionlimit(10 ** 6)


def move(cnt, n, visited):
    global time, way
    if time and cnt > time:
        return
    if (not time or cnt < time) and n == N:
        time = cnt
        way = 1
        return
    if cnt == time and n == N:
        way += 1
        return

    if n < N and not visited[n + 1]:
        visited[n + 1] = 1
        move(cnt + 1, n + 1, visited)
        visited[n + 1] = 0
    elif n % 2:
        if not visited[n + 1]:
            visited[n + 1] = 1
            move(cnt + 1, n + 1, visited)
            visited[n + 1] = 0
        if not visited[n - 1]:
            visited[n - 1] = 1
            move(cnt + 1, n - 1, visited)
            visited[n - 1] = 0
    elif N < (n * 3 // 4) and not visited[n // 2]:
        visited[n // 2] = 1
        move(cnt + 1, n // 2, visited)
        visited[n // 2] = 0
    elif N >= (n * 3 // 4) and not visited[n - 1]:
        move(cnt + n - N, N, visited)
    if N <= 2 and n == 2 and not visited[1]:
        visited[1] = 1
        move(cnt + 1, 1, visited)
        visited[1] = 0


N, K = map(int, input().split())
if K <= N:
    print(N - K)
    print(1)
else:
    time, way = 0, 0
    move(0, K, [0] * K + ([1, 0] if K % 2 else [1]))
    print(time)
    print(way)