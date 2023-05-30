import copy
from collections import deque

N = int(input())
N //= 3
n = 1
while True:
    if N == 1:
        break
    N //= 2
    n += 1

star = list([] for _ in range(n))
star[0] = list([deque([' ', ' ', '*', ' ', ' ']), deque([' ', '*', ' ', '*', ' ']), deque(['*', '*', '*', '*', '*'])])
for i in range(1, n):
    star[i] = copy.deepcopy(star[i - 1])
    for j in range(len(star[i - 1])):
        for k in range(3 * 2 ** (i - 1)):
            star[i][j].appendleft(' ')
            star[i][j].append(' ')
        star[i].append(star[i - 1][j] + deque([' ']) + star[i - 1][j])

for s in star[-1]:
    print("".join(s))