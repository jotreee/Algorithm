import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = A[:]
B.reverse()

result = list([1, 1] for _ in range(N))
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            result[i][0] = (result[j][0] + 1 if result[j][0] + 1 > result[i][0] else result[i][0])
        if B[j] < B[i]:
            result[N - 1 - i][1] = (result[N - 1 - j][1] + 1 if result[N - 1 - j][1] + 1 > result[N - 1 - i][1] else result[N - 1 - i][1])

answer = 0
for i in range(N):
    if result[i][0] + result[i][1] > answer:
        answer = result[i][0] + result[i][1]

print(answer - 1)