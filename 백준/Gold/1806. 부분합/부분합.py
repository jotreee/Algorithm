import sys
from collections import deque

input = sys.stdin.readline

N, S = map(int, input().split())
nums = deque(map(int, input().split()))
stack = deque()
s = 0

stack.append(nums.popleft())
s += stack[0]
result = 100001
for i in range(N):
    while True:
        if nums and s < S:
            s += nums[0]
            stack.append(nums.popleft())
        elif stack and s - stack[-1] >= S:
            s -= stack[-1]
            nums.appendleft(stack.pop())
        else:
            if s >= S and len(stack) < result:
                result = len(stack)
            break

    s -= stack[0]
    stack.popleft()

print(result if result != 100001 else 0)