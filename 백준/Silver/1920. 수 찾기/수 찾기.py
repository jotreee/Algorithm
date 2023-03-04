import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))
nums = deque(sorted(nums))
M = int(input().strip())
pros = list(map(int, input().split()))
for i in range(M):
    pros[i] = [pros[i], i]
pros.sort()

result = [0] * M
for n, m in pros:
    if n < nums[0]:
        continue
    for i in range(len(nums)):
        if n == nums[i]:
            result[m] = 1
            for _ in range(i):
                nums.popleft()
            break
        elif n < nums[i]:
            for _ in range(i):
                nums.popleft()
            break

for n in result:
    print(n)