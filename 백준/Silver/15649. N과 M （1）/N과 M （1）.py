def p(n, r, lst, visited):
    global result
    if not r:
        result.append(lst)
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = 1
            p(n, r - 1, lst + [str(i)], visited)
            visited[i] = 0


N, M = map(int, input().split())
result = []
p(N, M, [], [0] * (N + 1))
for i in range(len(result)):
    print(" ".join(result[i]))