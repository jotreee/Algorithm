import sys

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
result = []

num = 0
for n in arr:
    if n >= 0:
        num += n
    else:
        if num > 0:
            result.append(num)
        if num + n >= 0:
            num += n
        else:
            num = 0

if num > 0:
    result.append(num)

if result:
    print(max(result))
else:
    print(max(arr))