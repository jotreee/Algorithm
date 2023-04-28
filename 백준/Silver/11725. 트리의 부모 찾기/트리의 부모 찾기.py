import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
link = list([] for _ in range(N + 1))
for _ in range(N - 1):
    n, m = map(int, input().split())
    link[n].append(m)
    link[m].append(n)

result = [0] * (N + 1)
parent = deque([1])
while True:
    if parent:
        p = parent[0]
        for c in link[p]:
            if c != result[p]:
                result[c] = p
                parent.append(c)
        parent.popleft()
    else:
        break

for i in range(2, N + 1):
    print(result[i])