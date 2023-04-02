import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):

    k = int(input().strip())
    n = int(input().strip())
    apart = list([0] * n for _ in range(k + 1))

    for i in range(n):
        apart[0][i] = i + 1
    for i in range(1, k + 1):
        apart[i][0] = 1

    for i in range(1, k + 1):
        for j in range(1, n):
            apart[i][j] = apart[i - 1][j] + apart[i][j - 1]

    print(apart[k][n - 1])