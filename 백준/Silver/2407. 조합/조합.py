n, m = map(int, input().split())
if m > n - m:
    m = n - m

for i in range(n - m + 1, n):
    n *= i
for i in range(2, m):
    m *= i

print(n // m)