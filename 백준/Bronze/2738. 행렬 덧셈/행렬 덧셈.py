import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        matrix[i][j] += lst[j]
for i in range(N):
    print(" ".join(map(str, matrix[i])))