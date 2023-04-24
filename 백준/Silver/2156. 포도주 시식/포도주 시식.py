import sys

input = sys.stdin.readline

n = int(input().strip())
wine = list(int(input().strip()) for _ in range(n))
if n == 1:
    print(wine[0])
else:
    drink = list([] for _ in range(n))
    drink[0] = [0, 0, wine[0], 0]
    drink[1] = [wine[0], 0, wine[1], wine[0] + wine[1]]

    for i in range(2, n):
        drink[i] = [max(drink[i - 1][2], drink[i - 1][3]), drink[i - 1][0], max(drink[i - 1][0], drink[i - 1][1]) + wine[i], drink[i - 1][2] + wine[i]]

    print(max(drink[-1]))