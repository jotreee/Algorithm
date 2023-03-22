import sys

input = sys.stdin.readline

N, M = map(int, input().split())
game = [0] * 101
result = [0, 0, 1, 1, 1, 1, 1, 1] + [0] * 93

for i in range(101):
    game[i] = i
ladder = list(list(map(int, input().split())) for _ in range(N))
for i, j in ladder:
    game[i] = j
snake = list(list(map(int, input().split())) for _ in range(M))
for i, j in snake:
    game[i] = j

result = [0, 0, 1, 1, 1, 1, 1, 1] + [99] * 93
for i in range(2, 8):
    if i != game[i] and result[game[i]] > result[i]:
        result[game[i]] = result[i]

for _ in range(2):
    for i in range(8, 101):
        for j in range(1, 7):
            if result[i - j] + 1 < result[i]:
                result[i] = result[i - j] + 1
        if i != game[i] and result[game[i]] > result[i]:
            result[game[i]] = result[i]
        if i != game[i]:
            result[i] = 99

print(result[-1])