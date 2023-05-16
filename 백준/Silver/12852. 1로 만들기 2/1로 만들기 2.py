def cal(n, cnt, prev):
    global result
    if cnt >= result[0]:
        return
    if n == 1:
        result[0] = cnt
        result[1] = prev
        return
    if not n % 3:
        cal(n // 3, cnt + 1, prev + [n // 3])
    if not n % 2:
        cal(n // 2, cnt + 1, prev + [n // 2])
    if n > 1:
        cal(n - 1, cnt + 1, prev + [n - 1])


N = int(input().strip())
result = [1000001, []]
cal(N, 0, [N])
print(result[0])
print(" ".join(map(str, result[1])))