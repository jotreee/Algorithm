A, B, V = map(int, input().split())

if A > V:
    print(1)
elif (V - A) % (A - B):
    print((V - A) // (A - B) + 2)
else:
    print((V - A) // (A - B) + 1)