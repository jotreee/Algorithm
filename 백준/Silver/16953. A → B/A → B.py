def cal(n, cnt):
    global result
    if n == A:
        result = cnt
        return
    if not n % 2 and n // 2 >= A:
        cal(n // 2, cnt + 1)
    d = list(str(n))
    if d.pop() == '1' and int("".join(d)) >= A:
        cal(int("".join(d)), cnt + 1)


A, B = map(int, input().split())
result = 0
cal(B, 1)
if result:
    print(result)
else:
    print(-1)