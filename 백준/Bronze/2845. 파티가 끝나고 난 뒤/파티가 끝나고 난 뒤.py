N, M = map(int, input().split())
N *= M
arr = list(map(int, input().split()))
for i in range(len(arr)):
    arr[i] -= N
print(" ".join(map(str, arr)))