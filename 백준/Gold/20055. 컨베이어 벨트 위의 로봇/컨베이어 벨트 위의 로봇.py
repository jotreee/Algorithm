import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0]) * 2 * N

k = 0
for n in belt:
    if not n:
        k += 1

n = 0
r = []
while True:
    n += 1
    rmv = deque()
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    for i in range(len(r)):
        if r[i] == 2 * N - 1:
            r[i] = -1
        r[i] += 1

    for i in range(len(r)):
        if r[i] == 2 * N - 1:
            r[i] = -1
        if r[i] == N - 1:
            robot[N - 1] = 0
            rmv.appendleft(i)
        else:
            ri = r[i]
            if belt[ri + 1] > 0 and not robot[ri + 1]:
                robot[ri] = 0
                robot[ri + 1] = 1
                belt[ri + 1] -= 1
                r[i] += 1
                if ri + 1 == N - 1:
                    robot[N - 1] = 0
                    rmv.appendleft(i)
                if not belt[ri + 1]:
                    k += 1
    for i in rmv:
        del r[i]

    if belt[0] > 0 and not robot[0]:
        belt[0] -= 1
        robot[0] = 1
        r.append(0)
        if not belt[0]:
            k += 1
            
    if k >= K:
        print(n)
        break