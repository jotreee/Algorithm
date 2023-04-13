N = int(input())

num = 666
result = 0
idx = 0
while True:
    n = 0
    for k in list(str(num)):
        if k == '6':
            n += 1
        else:
            n = 0
        if n >= 3:
            result = num
            idx += 1
            break

    if idx == N:
        print(result)
        break
    else:
        num += 1