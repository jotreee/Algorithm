L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
a, b = A // C, B // D
if a * C < A:
    a += 1
if b * D < B:
    b += 1
print(L - max(a, b))