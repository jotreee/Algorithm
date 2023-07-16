alpha = [0] * 26
S = input()
for s in S:
    alpha[ord(s) - 97] += 1
print(" ".join(map(str, alpha)))