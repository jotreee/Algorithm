N = int(input())
nums = [1] * 10

for _ in range(N - 1):
    nxt = [0] * 10
    for i in range(10):
        for j in range(i, 10):
            nxt[j] += nums[i]
    nums = nxt

print(sum(nums) % 10007)