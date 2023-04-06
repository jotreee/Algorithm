import sys

input = sys.stdin.readline

N = int(input().strip())
nums = [0] * 10001
for _ in range(N):
    nums[int(input().strip())] += 1

for i in range(10001):
    if nums[i]:
        for _ in range(nums[i]):
            print(i)