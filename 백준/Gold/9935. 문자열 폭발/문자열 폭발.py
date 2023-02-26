import sys

input = sys.stdin.readline

string = input().strip()
bomb = input().strip()
len_bomb = len(bomb)
stack = []
end = bomb[-1]

for i in range(len(string)):
    stack.append(string[i])
    if stack[-1] == end and len(stack) >= len_bomb:
        for j in range(len_bomb):
            if stack[-len_bomb + j] != bomb[j]:
                break
        else:
            for _ in range(len_bomb):
                stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")