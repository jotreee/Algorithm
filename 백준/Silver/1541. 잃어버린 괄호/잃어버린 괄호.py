import sys

input = sys.stdin.readline

equation = input().strip()
nums = equation.replace("+", " ")
nums = nums.replace("-", " ")
nums = list(map(int, nums.split()))

plus = 1
for i in range(len(equation)):
    if equation[i] == '+':
        plus += 1
    elif equation[i] == '-':
        break

result = 0
for i in range(plus):
    result += nums[i]
for i in range(plus, len(nums)):
    result -= nums[i]

print(result)