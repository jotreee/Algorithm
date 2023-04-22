A, B = map(int, input().split())
C = int(input())

h = C // 60
m = C % 60

B += m
A += h
if B > 59:
    B -= 60
    A += 1
if A > 23:
    A %= 24
    
print(A, B)