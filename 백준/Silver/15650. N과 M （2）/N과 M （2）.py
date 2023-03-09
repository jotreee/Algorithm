def c(n, r, lst, idx):
    global result
    if not r:
        result.append(lst)
        return
    for i in range(idx + 1, n + 1):
        c(n, r - 1, lst + [str(i)], i)


N, M = map(int, input().split())
result = []
c(N, M, [], 0)
for i in range(len(result)):
    print(" ".join(result[i]))