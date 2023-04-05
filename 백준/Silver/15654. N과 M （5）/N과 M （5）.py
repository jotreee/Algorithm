import sys

input = sys.stdin.readline


def combi(r, visited, lst):
    global result, visit
    if not r:
        result.append(lst)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            combi(r - 1, visited, lst + [arr[i]])
            visited[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visit = [0] * N
result = []
combi(M, visit, [])
for i in range(len(result)):
    print(" ".join(map(str, result[i])))