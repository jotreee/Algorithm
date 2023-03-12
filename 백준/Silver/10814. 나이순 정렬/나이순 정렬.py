import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(list(input().split()) for _ in range(N))
for i in range(N):
    arr[i] += [i]

arr.sort(key=lambda x: (int(x[0]), x[2], x[1]))

for i in range(N):
    arr[i].pop()
    print(" ". join(arr[i]))