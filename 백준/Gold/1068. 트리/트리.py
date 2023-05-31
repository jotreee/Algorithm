import sys

input = sys.stdin.readline


def cut(p):
    global tree
    for n in tree[p][1]:
        cut(n)
    tree[p] = []

N = int(input().strip())
lst = list(map(int, input().split()))
tree = list([lst[i], []] for i in range(N))
for i in range(N):
    if lst[i] != -1:
        tree[lst[i]][1].append(i)

D = int(input().strip())
for i in range(N):
    if tree[i][1] and D in tree[i][1]:
        tree[i][1].remove(D)

cut(D)
result = 0
for i in range(N):
    if tree[i] and not tree[i][1]:
        result += 1
print(result)