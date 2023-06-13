N = int(input())
nums = list(map(int, input().split()))
num = int(input())
result = 0
for n in nums:
    if n == num:
        result += 1
print(result)