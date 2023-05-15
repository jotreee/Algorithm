import sys

input = sys.stdin.readline

S1 = list(input().strip())
S2 = list(input().strip())

LCS = list(list([0] * (len(S1) + 1)) for _ in range(len(S2) + 1))
for i in range(1, len(S2) + 1):
    for j in range(1, len(S1) + 1):
        if S2[i - 1] == S1[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = (LCS[i - 1][j] if LCS[i - 1][j] > LCS[i][j - 1] else LCS[i][j - 1])

print(LCS[-1][-1])