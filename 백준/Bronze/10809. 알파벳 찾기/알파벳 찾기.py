S = list(input())
result = [0] * 26
for i in range(97, 123):
    c = chr(i)
    if c in S:
        result[i - 97] = S.index(c)
    else:
        result[i - 97] = -1
print(" ".join(map(str, result)))