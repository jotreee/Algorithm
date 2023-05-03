def combination(n, r):
    r = (n - r if n - r < r else r)
    if r == 0:
        return 1
    elif r == 1:
        return n
    else:
        num1, num2 = 1, 1
        for i in range(n - r + 1, n + 1):
            num1 *= i
        for i in range(2, r + 1):
            num2 *= i
        return num1 // num2


N = int(input())
if N <= 2:
    print(1)
else:
    result = 0
    for i in range(N // 2 + 1 if N % 2 else N // 2):
        result += combination(N - i - 1, i)
    print(result)