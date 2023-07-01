S = [1, 1, 2, 2, 2, 8]
N = list(map(int, input().split()))
for i in range(6):
    S[i] -= N[i]
print(" ".join(map(str, S)))