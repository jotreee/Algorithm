N = int(input())
nums = [0] + [1] * 9

for _ in range(N - 1):
    nxt = [0] * 10
    nxt[1] += nums[0]
    nxt[8] += nums[9]
    for i in range(1, 9):
        nxt[i - 1] += nums[i]
        nxt[i + 1] += nums[i]
    nums = nxt

print(sum(nums) % 1000000000)