import sys

input = sys.stdin.readline


def func(idx, n, lst):
    global result
    if not n:
        result.append(lst)
        return
    for i in range(idx, N):
        func(i, n - 1, lst + [arr[i]])


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
func(0, M, [])
for l in result:
    print(" ".join(map(str, l)))