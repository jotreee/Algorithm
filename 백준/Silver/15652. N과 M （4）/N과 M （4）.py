def mklist(idx, n, arr):
    global result
    if not n:
        result.append(arr)
        return
    for i in range(idx, N + 1):
        mklist(i, n - 1, arr + [i])


N, M = map(int, input().split())
result = []
mklist(1, M, [])
for lst in result:
    print(" ".join(map(str, lst)))