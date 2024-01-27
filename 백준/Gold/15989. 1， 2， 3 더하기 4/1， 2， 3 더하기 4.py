import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    result = 0
    n = int(input().strip())
    for i in range(n // 3 + 1):
        num = n - i * 3
        result += (num // 2 + 1)
    print(result)