x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print(0)
elif (y3 - y1) * (x2 - x1) < (y2 - y1) * (x3 - x1):
    print(-1)
else:
    print(1)