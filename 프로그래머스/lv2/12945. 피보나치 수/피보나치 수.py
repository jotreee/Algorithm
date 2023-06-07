def solution(n):
    result = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        result[i] = result[i - 2] + result[i - 1]
        if result[i] >= 1234567:
            result[i] -= 1234567
    return result[-1]