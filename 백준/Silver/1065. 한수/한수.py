N = int(input())
if N < 100:
    print(N)
else:
    result = 99
    for i in range(100, N + 1):
        num = list(map(int, str(i)))
        d = num[1] - num[0]
        for j in range(len(num) - 2):
            if num[j + 2] - num[j + 1] != d:
                break
        else:
            result += 1
    print(result)