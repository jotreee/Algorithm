A, B = map(int, input().split())
w, l = (A + B) // 2, (A - B) // 2
if w < l or w < 0 or l < 0 or (A + B) % 2:
    print(-1)
else:
    print(w, l)