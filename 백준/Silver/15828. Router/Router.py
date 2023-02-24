import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
buffer = deque()
while True:
    n = int(input().strip())
    if n == -1:
        break
    if n == 0:
        buffer.popleft()
    if n != 0 and len(buffer) < N:
        buffer.append(str(n))
if len(buffer) == 0:
    print("empty")
else:
    print(" ".join(buffer))