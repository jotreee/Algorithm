import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(int(input().strip()) for _ in range(N))
print(round(sum(arr) / N))

arr.sort()
print(arr[N // 2])

nums = [0] * 8001
for n in arr:
    nums[n + 4000] += 1
idx = nums.index(max(nums))
snums = (sorted(nums))
snums.reverse()

if snums[0] == snums[1]:
    nums[idx] -= 1
    idx = nums.index(max(nums))
print(idx - 4000)

print(arr[-1] - arr[0])