import sys

input = sys.stdin.readline

N, B = map(int, input().split())
n = B
cnt = 0
while True:
    n //= 2
    cnt += 1
    if n < 1:
        break

store = list([] for _ in range(cnt))
store[0] = list(list(map(int, input().split())) for _ in range(N))
for i in range(N):
    for j in range(N):
        if store[0][i][j] >= 1000:
            store[0][i][j] %= 1000
for n in range(1, cnt):
    new = list(list([0] * N) for _ in range(N))
    A = store[n - 1]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new[i][j] += A[i][k] * A[k][j]
            if new[i][j] >= 1000:
                new[i][j] %= 1000
    store[n] = new

result = store[cnt - 1]
B -= 2 ** (cnt - 1)
for n in range(cnt - 2, -1, -1):
    now = list(list([0] * N) for _ in range(N))
    if 2 ** n <= B:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    now[i][j] += store[n][i][k] * result[k][j]
                if now[i][j] >= 1000:
                    now[i][j] %= 1000
        B -= 2 ** n
        result = now
        if not B:
            break

for i in range(N):
    print(" ".join(map(str, result[i])))