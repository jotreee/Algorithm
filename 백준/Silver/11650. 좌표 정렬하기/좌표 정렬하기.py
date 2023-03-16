import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(list(map(int, input().split())) for _ in range(N))
arr.sort()

for i in range(N):
    print(" ".join(map(str, arr[i])))