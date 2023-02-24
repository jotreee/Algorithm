import sys

input = sys.stdin.readline


def combi(r):
    num1, num2 = 1, 1
    s = N - r
    r = max(N - 2 * r, r)

    for i in range(r + 1, s + 1):
        num1 *= i

    for j in range(2, s - r + 1):
        num2 *= j

    return num1 // num2


N = int(input().strip())
result = 0

for n in range(N // 2 + 1):
    result += combi(n) * 2 ** n

print(result % 10007)