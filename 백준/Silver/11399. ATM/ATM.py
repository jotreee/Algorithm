import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
arr.sort()

result = 0
for i in range(N):
    result += arr[i] * (N - i)

print(result)