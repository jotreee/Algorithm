import sys

input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == '.':
        break
    stack = []
    for i in range(len(sentence)):
        if sentence[i] == '(':
            stack.append('(')
        elif sentence[i] == '[':
            stack.append('[')
        elif sentence[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif sentence[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')