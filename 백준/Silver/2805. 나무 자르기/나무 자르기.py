import sys

input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()
tree.reverse()

cut = [0] * N
found = 0
for i in range(1, N):
    cut[i] = cut[i - 1] + (tree[i - 1] - tree[i]) * i
    if cut[i] >= M:
        height = cut[i]
        n = 0
        found = 1
        while True:
            if height - i * n == M:
                print(tree[i] + n)
                break
            elif height - i * n < M:
                print(tree[i] + n - 1)
                break
            else:
                n += 1
    if found:
        break

else:
    height = cut[-1]
    n = 0
    while True:
        if height + N * n >= M:
            print(tree[N - 1] - n)
            break
        else:
            n += 1