import sys
from collections import deque

input = sys.stdin.readline

arr = deque()
N = int(input().strip())
for _ in range(N):
    order = input().split()
    if order[0] == 'push_front':
        arr.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        arr.append(int(order[1]))
    elif order[0] == 'pop_front':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(arr))
    elif order[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    else:
        if arr:
            print(arr[-1])
        else:
            print(-1)