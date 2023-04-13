import sys

input = sys.stdin.readline

N = int(input().strip())
result = [0] * N
body = list(list(map(int, input().split())) for _ in range(N))

for i in range(N):
    n = 1
    for j in range(N):
        if body[j][0] > body[i][0] and body[j][1] > body[i][1]:
            n += 1
    result[i] = n

print(" ".join(map(str, result)))