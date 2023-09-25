N = int(input())
paper = list(list([0] * 100) for _ in range(100))
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[a + i][b + j] += 1

result = 0
for i in range(100):
    for j in range(100):
        result += (1 if paper[i][j] else 0)

print(result)