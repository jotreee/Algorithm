import sys
from collections import deque

input = sys.stdin.readline


def trans(n, order, now):
    if order == 'D':
        return [(2 * n) % 10000, now + 'D']
    elif order == 'S':
        if not n:
            n = 9999
        else:
            n -= 1
        return [n, now + 'S']
    elif order == 'L':
        a = n // 1000
        n %= 1000
        b = n // 100
        n %= 100
        c = n // 10
        d = n % 10
        return [b * 1000 + c * 100 + d * 10 + a, now + 'L']
    else:
        a = n // 1000
        n %= 1000
        b = n // 100
        n %= 100
        c = n // 10
        d = n % 10
        return [d * 1000 + a * 100 + b * 10 + c, now + 'R']


T = int(input().strip())
orders = ['D', 'S', 'L', 'R']

for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    arr = deque([[A, '']])
    visited[A] = 1
    end = 0
    while True:
        n, o = arr[0][0], arr[0][1]
        for k in range(4):
            new = trans(n, orders[k], o)
            if new[0] == B:
                print(new[1])
                end = 1
                break
            if new[0] != B and not visited[new[0]]:
                arr.append(new)
                visited[new[0]] = 1
        if end:
            break
        arr.popleft()