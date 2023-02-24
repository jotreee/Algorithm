from collections import deque

str = deque(input())
pipe = 0
result = 0

while len(str) > 0:
    if str[0] == '(':
        if str[1] == ')':
            result += pipe
            str.popleft()
            str.popleft()
        else:
            pipe += 1
            str.popleft()
    else:
        pipe -= 1
        result += 1
        str.popleft()

print(result)