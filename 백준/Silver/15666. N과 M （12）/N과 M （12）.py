import sys

input = sys.stdin.readline


def make(idx, n, lst):
    global result
    if not n:
        result.append(lst)
        return
    for i in range(idx, 10001):
        if nums[i]:
            make(i, n - 1, lst + [i])


N, M = map(int, input().split())
arr = list(map(int, input().split()))
nums = [0] * 10001
for n in arr:
    nums[n] = 1

result = []
make(0, M, [])
for l in result:
    print(" ".join(map(str, l)))