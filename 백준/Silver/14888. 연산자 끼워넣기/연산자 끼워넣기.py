def plus(a, b): # 1
    return a + b

def minus(a, b): # 2
    return a - b

def multiple(a, b): # 3
    return a * b

def divide(a, b): # 4
    if a < 0:
        return -(-a//b)
    else:
        return a//b

def calculate(n, cal_n, now): # 몇 번째인지, 사칙연산 남은 횟수, 현재 계산 결과
    global arr, cal, result
    if n == N - 1:
        result.append(now)
        return
    else:
        if cal_n[0] > 0:
            cal_n[0] -= 1
            calculate(n + 1, cal_n, now + arr[n + 1])
            cal_n[0] += 1
        if cal_n[1] > 0:
            cal_n[1] -= 1
            calculate(n + 1, cal_n, now - arr[n + 1])
            cal_n[1] += 1
        if cal_n[2] > 0:
            cal_n[2] -= 1
            calculate(n + 1, cal_n, now * arr[n + 1])
            cal_n[2] += 1
        if cal_n[3] > 0:
            cal_n[3] -= 1
            if now < 0:
                calculate(n + 1, cal_n, -(-now // arr[n + 1]))
            else:
                calculate(n + 1, cal_n, now // arr[n + 1])
            cal_n[3] += 1

N = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))
result = []
calculate(0, cal, arr[0])
print(max(result))
print(min(result))