import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
for n in range(1, N + 1):
    nums[n] += nums[n - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(nums[j] - nums[i - 1])