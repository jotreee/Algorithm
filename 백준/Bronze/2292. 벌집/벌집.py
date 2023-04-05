N = int(input())
n = 1
i = 0
while True:
    if N <= n + i * 6:
        print(i + 1)
        break
    n += i * 6
    i += 1