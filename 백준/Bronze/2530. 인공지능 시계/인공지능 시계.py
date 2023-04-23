A, B, C = map(int, input().split())
D = int(input())

h = D // 3600
m = (D % 3600) // 60
s = D % 60

C += s
if C > 59:
    C %= 60
    m += 1
B += m
if B > 59:
    B %= 60
    A += 1
A += h
if A > 23:
    A %= 24

print(A, B, C)