from collections import deque
def solution(s):
    s = deque(s)
    stack = [s.popleft()]
    while True:
        if s:
            if stack and stack[-1] == s[0]:
                stack.pop()
                s.popleft()
            else:
                stack.append(s.popleft())
        else:
            if stack:
                return 0
                break
            else:
                return 1
                break