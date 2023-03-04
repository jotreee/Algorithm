import sys

input = sys.stdin.readline

while True:
    num = input().strip()
    if not int(num):
        break
    else:
        for i in range(len(num) // 2):
            if num[i] != num[-i -1]:
                print("no")
                break
        else:
            print("yes")