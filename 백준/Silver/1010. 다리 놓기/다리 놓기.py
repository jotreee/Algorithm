import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    r, n = map(int, input().split())
    r = (n - r if r < n - r else r)
    num1, num2 = 1, 1
    for i in range(n - r + 1, n + 1):
        num1 *= i
    for i in range(2, r + 1):
        num2 *= i
    print(num1 // num2)