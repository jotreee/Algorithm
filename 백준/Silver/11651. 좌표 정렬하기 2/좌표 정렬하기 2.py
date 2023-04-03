import sys

input = sys.stdin.readline

N = int(input().strip())
spot = list(list(map(int, input().split())) for _ in range(N))
spot.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(" ".join(map(str, spot[i])))