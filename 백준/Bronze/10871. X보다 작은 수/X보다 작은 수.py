N, X = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for n in arr:
    if n < X:
        result.append(n)

print(' '.join(map(str, result)))