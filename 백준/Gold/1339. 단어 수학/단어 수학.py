import sys

input = sys.stdin.readline

N = int(input().strip())
alpha = [[0, i] for i in range(26)]
for _ in range(N):
    word = list(input().strip())
    for i in range(len(word), 0, -1):
        alpha[ord(word[-i]) - 65][0] += 10 ** (i - 1)

alpha.sort()
alpha.reverse()

result = 0
for i in range(9):
    result += alpha[i][0] * (9 - i)
print(result)