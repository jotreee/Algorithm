from collections import deque

N = int(input())
nums = deque([])
for i in range(N):
    nums.append(int(input()))
nums = deque(sorted(list(nums)))

result = deque([])
divides = deque([])

if N == 2:
    dif = nums[1] - nums[0]
    for i in range(2, dif + 1):
        if dif % i == 0:
            divides.append(i)
else:
    dif1 = nums[1] - nums[0]
    dif2 = nums[2] - nums[1]
    for i in range(2, min(dif1, dif2) + 1):
        if dif1 % i == 0 and dif2 % i == 0:
            divides.append(i)

for divide in divides:
    quot = nums[0] % divide
    for i in range(1, N-1):
        if quot != nums[i] % divide:
            break
    else:
        result.append(str(divide))
print(" ".join(result))