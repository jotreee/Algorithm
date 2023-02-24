import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))

for i in range(N):
    arr[i] = [arr[i], i]
arr.sort()

result = [0] * N
smaller = 0
for i in range(N):
    result[arr[i][1]] = str(smaller)
    if i < N - 1 and arr[i][0] < arr[i + 1][0]:
        smaller += + 1

print(" ".join(result))