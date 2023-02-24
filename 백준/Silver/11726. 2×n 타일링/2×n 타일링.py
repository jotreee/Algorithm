def fact(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


N = int(input())

result = 0
for n in range(N // 2 + 1):
    result += (fact(N - n) // (fact(N - 2 * n) * fact(n)))

print(result % 10007)