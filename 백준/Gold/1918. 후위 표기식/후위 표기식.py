from collections import deque

origin = deque(input())
symbol = deque([])
result = ''

for s in origin:
    if s == '(':
        symbol.append(s)
    elif s == ')':
        while True:
            if symbol[-1] == '(':
                symbol.pop()
                break
            result += symbol.pop()
    elif s == '*' or s == '/':
        if symbol and symbol[-1] == '*' or symbol and symbol[-1] == '/':
            result += symbol.pop()
        symbol.append(s)
    elif s == '+' or s == '-':
        if symbol and symbol[-1] == '+' or symbol and symbol[-1] == '-':
            result += symbol.pop()
        elif symbol and symbol[-1] != '(':
            while True:
                result += symbol.pop()
                if not symbol or symbol[-1] == '(':
                    break
        symbol.append(s)
    else:
        result += s

if symbol:
    while True:
        result += symbol.pop()
        if not symbol:
            break

print(result)