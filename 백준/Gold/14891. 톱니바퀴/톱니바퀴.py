# N = 0, S = 1
# 12시부터 시계방향으로 input -> 2, 6
# 12시에 S극이면 1, 2, 4, 8

from collections import deque

A = deque(map(int, input()))
B = deque(map(int, input()))
C = deque(map(int, input()))
D = deque(map(int, input()))

N = int(input())

for tc in range(N):

    combi = [0, 0, 0]
    if A[2] != B[6]:
        combi[0] = 1
    if B[2] != C[6]:
        combi[1] = 1
    if C[2] != D[6]:
        combi[2] = 1

    turn = list(map(int, input().split()))

    if turn[0] == 1:
        if turn[1] == 1:
            A.appendleft(A.pop())
            if combi[0] == 1:
                B.append(B.popleft())
                if combi[1] == 1:
                    C.appendleft(C.pop())
                    if combi[2] == 1:
                        D.append(D.popleft())
        else:
            A.append(A.popleft())
            if combi[0] == 1:
                B.appendleft(B.pop())
                if combi[1] == 1:
                    C.append(C.popleft())
                    if combi[2] == 1:
                        D.appendleft(D.pop())

    elif turn[0] == 2:
        if turn[1] == 1:
            B.appendleft(B.pop())
            if combi[0] == 1:
                A.append(A.popleft())
            if combi[1] == 1:
                C.append(C.popleft())
                if combi[2] == 1:
                    D.appendleft(D.pop())
        else:
            B.append(B.popleft())
            if combi[0] == 1:
                A.appendleft(A.pop())
            if combi[1] == 1:
                C.appendleft(C.pop())
                if combi[2] == 1:
                    D.append(D.popleft())

    elif turn[0] == 3:
        if turn[1] == 1:
            C.appendleft(C.pop())
            if combi[1] == 1:
                B.append(B.popleft())
                if combi[0] == 1:
                    A.appendleft(A.pop())
            if combi[2] == 1:
                D.append(D.popleft())
        else:
            C.append(C.popleft())
            if combi[1] == 1:
                B.appendleft(B.pop())
                if combi[0] == 1:
                    A.append(A.popleft())
            if combi[2] == 1:
                D.appendleft(D.pop())

    else:
        if turn[1] == 1:
            D.appendleft(D.pop())
            if combi[2] == 1:
                C.append(C.popleft())
                if combi[1] == 1:
                    B.appendleft(B.pop())
                    if combi[0] == 1:
                        A.append(A.popleft())
        else:
            D.append(D.popleft())
            if combi[2] == 1:
                C.appendleft(C.pop())
                if combi[1] == 1:
                    B.append(B.popleft())
                    if combi[0] == 1:
                        A.appendleft(A.pop())


result = 0
if A[0] == 1:
    result += 1
if B[0] == 1:
    result += 2
if C[0] == 1:
    result += 4
if D[0] == 1:
    result += 8

print(result)