N = int(input())
if int(N ** 0.5) ** 2 == N:
    print(1)
else:
    a = int(N ** 0.5)
    for i in range(1, a + 1):
        b = int((N - i ** 2) ** 0.5)
        if i ** 2 + b ** 2 == N:
            print(2)
            break
    else:
        end = 0
        for i in range(1, a + 1):
            b = int((N - i ** 2) ** 0.5)
            for j in range(1, b + 1):
                c = int((N - i ** 2 - j ** 2) ** 0.5)
                if i ** 2 + j ** 2 + c ** 2 == N:
                    print(3)
                    end = 1
                    break
            if end:
                break
        else:
            print(4)