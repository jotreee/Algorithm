import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
lst = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j] and lst[i] <= lst[j]:
            lst[i] = lst[j] + 1

n = max(lst)
print(n)
result = []
for i in range(N - 1, -1, -1):
    if lst[i] == n:
        result.append(arr[i])
        n -= 1
    if not n:
        break

print(" ".join(map(str, reversed(result))))