R, C, T = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(R)]

# 공기 청정기 위치
air = 0
for i in range(R):
    if Map[i][0] == -1:
        air = i
        break

for tc in range(T):

    # 먼지 확산
    dust = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if Map[i][j] > 0:
                d = Map[i][j] // 5
                n = 0
                if i > 0 and Map[i - 1][j] >= 0:
                    dust[i - 1][j] += d
                    n += 1
                if i < R - 1 and Map[i + 1][j] >= 0:
                    dust[i + 1][j] += d
                    n += 1
                if j > 0 and Map[i][j - 1] >= 0:
                    dust[i][j - 1] += d
                    n += 1
                if j < C - 1 and Map[i][j + 1] >= 0:
                    dust[i][j + 1] += d
                    n += 1
                dust[i][j] -= n * d

    for i in range(R):
        for j in range(C):
            Map[i][j] += dust[i][j]
            
    # 먼지 순환
    new = [[0] * C for _ in range(R)]
    for i in range(R):
        new[i] = Map[i][:]

    # 가로
    for i in range(C - 1):
        new[air][i + 1] = Map[air][i]
        new[air + 1][i + 1] = Map[air + 1][i]
        new[0][i] = Map[0][i + 1]
        new[R - 1][i] = Map[R - 1][i + 1]

    # 윗쪽 세로
    for i in range(air):
        new[i + 1][0] = Map[i][0]
        new[i][C - 1] = Map[i + 1][C - 1]

    # 아랫쪽 세로
    for i in range(air + 1, R - 1):
        new[i][0] = Map[i + 1][0]
        new[i + 1][C - 1] = Map[i][C - 1]

    new[air][0] = -1
    new[air + 1][0] = -1
    new[air][1] = 0
    new[air + 1][1] = 0

    for i in range(R):
        Map[i] = new[i][:]

result = 0
for i in range(R):
    result += sum(Map[i])

print(result + 2)