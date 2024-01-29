N = int(input())
num = list(map(int, input().split()))
result = [0] + [N + 1] * (N - 1)
for i in range(N - 1):
    for j in range(1, num[i] + 1):
        if i + j < N and result[i] + 1 < result[i + j]:
            result[i + j] = result[i] + 1

print(result[-1] if result[-1] <= N else -1)