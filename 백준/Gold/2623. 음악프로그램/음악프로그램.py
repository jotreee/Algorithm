import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
seq = list(deque(map(int, input().split())) for _ in range(M))
for i in range(M):
    seq[i].popleft()
mem = list([0] * (N + 1) for _ in range(M))
nums = [0] * (N + 1)
result = []
for i in range(M):
    for n in seq[i]:
        mem[i][n] = 1

while True:
    appended = 0
    for i in range(M):
        if seq[i]:
            n = seq[i][0]
            for j in range(M):
                if seq[j] and mem[j][n] and seq[j][0] != n:
                    break
            else:
                appended = 1
                result.append(n)
                nums[n] = 1
                for j in range(M):
                    if seq[j] and seq[j][0] == n:
                        seq[j].popleft()
                        mem[j][n] = 0

    if not appended:
        for i in range(M):
            if seq[i]:
                print(0)
                break
        else:
            for i in range(1, N + 1):
                if not nums[i]:
                    result.append(i)
            for n in result:
                print(n)
        break