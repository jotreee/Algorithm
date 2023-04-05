import sys

input = sys.stdin.readline

K = int(input().strip())
result = []

for _ in range(K):
    n = int(input().strip())
    if n:
        result.append(n)
    else:
        result.pop()

print(sum(result))