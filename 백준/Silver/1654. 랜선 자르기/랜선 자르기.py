import sys

input = sys.stdin.readline

K, N = map(int, input().split())
line = list(int(input().strip()) for _ in range(K))
line.sort()
divide = [0] * K
remain = [0] * K

n = sum(line) // N
while True:
    idx = 0
    for i in range(K):
        divide[i] = line[i] // n
        remain[i] = line[i] % n
        if remain[i] > remain[idx]:
            idx = i

    if sum(divide) >= N:
        while True:
            n += 1
            s = 0
            for i in range(K):
                s += line[i] // n
            if s < N:
                print(n - 1)
                break
        break

    else:
        n = line[idx] // (divide[idx] + 1)