def queen(idx, visited):
    global result
    if idx == N:
        result += 1
        return
    for i in range(N):
        if not visited[idx][i]:
            for j in range(idx + 1, N):
                visited[j][i] += 1
                if 0 <= i + j - idx < N:
                    visited[j][i + j - idx] += 1
                if 0 <= i - j + idx < N:
                    visited[j][i - j + idx] += 1
            queen(idx + 1, visited)
            for j in range(idx + 1, N):
                visited[j][i] -= 1
                if 0 <= i + j - idx < N:
                    visited[j][i + j - idx] -= 1
                if 0 <= i - j + idx < N:
                    visited[j][i - j + idx] -= 1


N = int(input())
chess = list([0] * N for _ in range(N))
result = 0
queen(0, list([0] * N for _ in range(N)))
print(result)