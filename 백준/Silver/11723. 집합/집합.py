import sys
input = sys.stdin.readline

S = [0] * 21
N = int(input().strip())
for i in range(N):
    order = input().split()
    if order[0] == 'add':
        S[int(order[1])] = 1
    elif order[0] == 'remove':
        S[int(order[1])] = 0
    elif order[0] == 'check':
        if S[int(order[1])] == 0:
            print(0)
        else:
            print(1)
    elif order[0] == 'toggle':
        if S[int(order[1])] == 0:
            S[int(order[1])] = 1
        else:
            S[int(order[1])] = 0
    elif order[0] == 'all':
        S = [1] * 21
    elif order[0] == 'empty':
        S = [0] * 21