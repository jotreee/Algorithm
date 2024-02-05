N = int(input())
nums = list(map(int, input().split()))
cal = list(list([0] * 21) for _ in range(N - 1))
cal[0][nums[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if cal[i - 1][j]:
            if j + nums[i] <= 20:
                cal[i][j + nums[i]] += cal[i - 1][j]
            if j - nums[i] >= 0:
                cal[i][j - nums[i]] += cal[i - 1][j]

print(cal[-1][nums[-1]])