import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
MAP = list(list(map(int, input().split())) for _ in range(N))
order = list(map(int, input().split()))
dice = [0] * 6

for D in order:
    if D == 1 and y + 1 <= M - 1:
        y += 1
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif D == 2 and y - 1 >= 0:
        y -= 1
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif D == 3 and x - 1 >= 0:
        x -= 1
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    elif D == 4 and x + 1 <= N - 1:
        x += 1
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    else:
        continue
    if MAP[x][y]:
        dice[0] = MAP[x][y]
        MAP[x][y] = 0
    else:
        MAP[x][y] = dice[0]
    print(dice[5])