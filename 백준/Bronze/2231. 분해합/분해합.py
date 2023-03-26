N = int(input())
for i in range(1, N):
    if i + sum(map(int, list(str(i)))) == N:
        print(i)
        break
else:
    print(0)