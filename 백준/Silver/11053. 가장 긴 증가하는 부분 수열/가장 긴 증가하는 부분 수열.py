import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
result = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and result[j] >= result[i]:
            result[i] = result[j] + 1

print(max(result))