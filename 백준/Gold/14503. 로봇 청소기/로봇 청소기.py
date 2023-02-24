N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
clean = 0

while True:
    if arr[r][c] == 1:
        break
    elif arr[r][c] == 0:
        clean += 1
        arr[r][c] = 2
    for i in range(4):
        d -= 1
        if d < 0:
            d += 4
        if arr[r + dr[d]][c + dc[d]] == 0:
            r += dr[d]
            c += dc[d]
            break
    else:
        r += dr[d - 2]
        c += dc[d - 2]

print(clean)