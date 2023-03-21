N, K = map(int, input().split())
arr = [0] * N
for i in range(N):
    arr[i] = i + 1
result = [0] * N
n = K - 1
idx = 0

while True:
    if n < len(arr):
        result[idx] = arr.pop(n)
        idx += 1
        n += K - 1
    else:
        n -= len(arr)
    if not arr:
        break

print('<'+", ".join(map(str, result))+'>')