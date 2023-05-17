import sys
from collections import deque

input = sys.stdin.readline

V, E = map(int, input().split())
node = [0] * (V + 1)
edge = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edge.append([C, A, B])
edge.sort()

result = 0
n = 0
for k, i, j in edge:
    if not node[i] or not node[j]:
        if node[i] and not node[j]:
            node[j] = node[i]
        elif node[j] and not node[i]:
            node[i] = node[j]
        else:
            n += 1
            node[i], node[j] = n, n
        result += k
    elif node[i] != node[j]:
        add = node[j]
        for x in range(V + 1):
            if node[x] == add:
                node[x] = node[i]
        result += k

print(result)