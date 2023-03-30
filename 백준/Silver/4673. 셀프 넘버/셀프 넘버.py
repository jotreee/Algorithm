nums = [0] + [1] * 10000
for i in range(1, 10001):
    if nums[i]:
        n = i
        while True:
            n += sum(map(int, list(str(n))))
            if n <= 10000 and nums[n]:
                nums[n] = 0
            else:
                break

for i in range(1, 10001):
    if nums[i]:
        print(i)