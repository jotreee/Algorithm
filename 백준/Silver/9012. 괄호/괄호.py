import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):

    string = input().strip()
    n = 0

    for i in range(len(string)):
        if string[i] == '(':
            n += 1
        else:
            n -= 1
        if n < 0:
            print("NO")
            break
            
    else:
        if n:
            print("NO")
        else:
            print("YES")