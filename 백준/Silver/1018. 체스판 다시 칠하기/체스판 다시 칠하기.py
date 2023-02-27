import sys

input = sys.stdin.readline

N, M = map(int, input().split())
chess = list(list(input().strip()) for _ in range(N))
result = []

for i in range(N - 7):
    for j in range(M - 7):
        black = 0
        white = 0
        for k in range(8):
            for l in range(8):
                if ((k + l) % 2 and chess[i + k][j + l] == 'B') or (not (k + l) % 2 and chess[i + k][j + l] == 'W'):
                    black += 1
                if ((k + l) % 2 and chess[i + k][j + l] == 'W') or (not (k + l) % 2 and chess[i + k][j + l] == 'B'):
                    white += 1
        result.append(white)
        result.append(black)

print(min(result))