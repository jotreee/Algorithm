import sys

input = sys.stdin.readline

S1 = list(input().strip())
S2 = list(input().strip())

LCS = list(list([0, []] for _ in range(len(S2) + 1)) for _ in range(len(S1) + 1))
for i in range(1, len(S1) + 1):
    for j in range(1, len(S2) + 1):
        if S1[i - 1] == S2[j - 1] and LCS[i - 1][j - 1][0] >= LCS[i - 1][j][0] and LCS[i - 1][j - 1][0] >= LCS[i][j - 1][0]:
            LCS[i][j] = [LCS[i - 1][j - 1][0] + 1, LCS[i - 1][j - 1][1] + [S1[i - 1]]]
        else:
            LCS[i][j] = (LCS[i - 1][j] if LCS[i - 1][j][0] >= LCS[i][j - 1][0] else LCS[i][j - 1])

print(LCS[-1][-1][0])
print("".join(LCS[-1][-1][1]))