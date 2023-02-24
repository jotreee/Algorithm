N, L = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
way = 0
for i in range(N):
    height = Map[i][0]
    check = [1] + [0] * (N - 1)
    for j in range(N):
        if abs(Map[i][j] - height) > 1:
            break
        elif Map[i][j] - height == 1: # 오르막
            if j > 0 and check[j - 1] < L:
                break
            check[j] = 1
        elif Map[i][j] - height == -1: # 내리막
            if j > 0 > check[j - 1] > -L:
                break
            check[j] = -1
        else:
            if j > 0:
                if check[j - 1] > 0:
                    check[j] = check[j - 1] + 1
                else:
                    if check[j - 1] == -L:
                        check[j] = 1
                    else:
                        check[j] = check[j - 1] - 1
        if j == N - 1 and 0 > check[j] > -L:
            break
        height = Map[i][j]
    else:
        way += 1

    height = Map[0][i]
    check = [1] + [0] * (N - 1)
    for j in range(N):
        if abs(Map[j][i] - height) > 1:
            break
        elif Map[j][i] - height == 1:  # 오르막
            if j > 0 and check[j - 1] < L:
                break
            check[j] = 1
        elif Map[j][i] - height == -1:  # 내리막
            if j > 0 > check[j - 1] > -L:
                break
            check[j] = -1
        else:
            if j > 0:
                if check[j - 1] > 0:
                    check[j] = check[j - 1] + 1
                else:
                    if check[j - 1] == -L:
                        check[j] = 1
                    else:
                        check[j] = check[j - 1] - 1
        if j == N - 1 and -L < check[j] < 0:
            break
        height = Map[j][i]
    else:
        way += 1

print(way)