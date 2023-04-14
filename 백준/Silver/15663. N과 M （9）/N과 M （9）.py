import sys

input = sys.stdin.readline


def make(idx, n, lst, visited):
    global result
    if not n:
        result.append(lst)
        return
    if idx == 10001:
        return
    for i in range(10001):
        if visited[i]:
            visited[i] -= 1
            make(i, n - 1, lst + [i], visited)
            visited[i] += 1


N, M = map(int, input().split())
arr = list(map(int, input().split()))
nums = [0] * 10001
for n in arr:
    nums[n] += 1

result = []
make(0, M, [], nums)
for l in result:
    print(" ".join(map(str, l)))