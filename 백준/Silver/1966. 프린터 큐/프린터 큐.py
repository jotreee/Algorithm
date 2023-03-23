import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    Q = deque(map(int, input().split()))
    importance = deque(reversed(sorted(Q)))
    Q[M] = -Q[M]

    i = 1
    while True:
        if Q[0] < 0:
            if -Q[0] == importance[0]:
                print(i)
                break
            else:
                Q.append(Q.popleft())
        else:
            if Q[0] == importance[0]:
                Q.popleft()
                importance.popleft()
                i += 1
            else:
                Q.append(Q.popleft())