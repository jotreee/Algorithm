from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
    print(N)

elif N > K:
    print(N - K)
    print(" ".join(map(str, list(range(N, K - 1, -1)))))

else:
    visited = [0] * K + ([1, 0] if K % 2 else [1])
    find = deque([[K]])
    while True:
        lst = find.popleft()
        n = lst[0]
        if n + 1 == N or n - 1 == N or (not n % 2 and n // 2 == N):
            print(len(lst))
            print(" ".join(map(str, [N] + lst)))
            break

        if n % 2:
            if not visited[n - 1]:
                visited[n - 1] = 1
                find.append([n - 1] + lst)
            if not visited[n + 1]:
                visited[n + 1] = 1
                find.append([n + 1] + lst)
        elif n < N and not visited[n + 1]:
            visited[n + 1] = 1
            find.append([n + 1] + lst)
        elif N < (3 * n // 4) and not visited[n // 2]:
            visited[n // 2] = 1
            find.append([n // 2] + lst)
        elif not visited[n - 1]:
            visited[n - 1] = 1
            find.append([n - 1] + lst)