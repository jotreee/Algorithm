N = int(input())
n = 0
while True:
    N //= 3
    n += 1
    if N == 1:
        break

stars = list([] for _ in range(n))
stars[0] = ['***', '* *', '***']
for i in range(1, n):
    for j in range(3 ** i):
        stars[i].append(stars[i - 1][j] * 3)
    for j in range(3 ** i):
        stars[i].append(stars[i - 1][j] + ' ' * 3 ** i + stars[i - 1][j])
    for j in range(3 ** i):
        stars[i].append(stars[i - 1][j] * 3)

for i in range(len(stars[-1])):
    print(stars[-1][i])