import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = deque(int(input().strip()) for _ in range(n))
nums = [0] * n
for i in range(1, n + 1):
    nums[-i] = i
stack = []
result = []

for i in range(n):
    if stack and stack[-1] == arr[i]:
        stack.pop()
        result.append('-')
    elif arr[i] > i:
        while True:
            if nums:
                stack.append(nums.pop())
                result.append('+')
                if stack[-1] == arr[i]:
                    stack.pop()
                    result.append('-')
                    break
            else:
                break
    else:
        result = []
        break

if result:
    for s in result:
        print(s)
else:
    print('NO')