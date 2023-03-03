import sys, copy
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
arr = list(list(map(int, input().split())) for _ in range(N))

connect = list([] for _ in range(N))
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            connect[i].append(j)

result = list(['0'] * N for _ in range(N))
for i in range(N):
    connected = deque(connect[i])
    while True:
        for j in copy.deepcopy(connected):
            result[i][j] = '1'
            for k in connect[j]:
                if result[i][k] == '0':
                    connected.append(k)
            connected.popleft()

        if not connected:
            break

for i in range(N):
    print(" ".join(result[i]))