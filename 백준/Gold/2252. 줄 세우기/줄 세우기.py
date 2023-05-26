import sys

input = sys.stdin.readline

N, M = map(int, input().split())
line = list([[], []] for _ in range(N + 1))
check = [0] * (N + 1)
result = []
for _ in range(M):
    a, b = map(int, input().split())
    line[a][1].append(b)
    line[b][0].append(a)

while True:
    prior = []
    for i in range(1, N + 1):
        if not check[i] and not line[i][0]:
            prior.append(i)
    if not prior:
        print(" ".join(map(str, result)))
        break

    for p in prior:
        for n in line[p][1]:
            line[n][0].remove(p)
        check[p] = 1
        result.append(p)