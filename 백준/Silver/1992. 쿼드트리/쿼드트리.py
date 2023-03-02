import sys

input = sys.stdin.readline


def cut(x, y, n):
    press = ''
    for k in range(4):
        num = image[y + dr[k] * n][x + dc[k] * n]
        end = 0
        for i in range(y + dr[k] * n, y + dr[k] * n + n):
            for j in range(x + dc[k] * n, x + dc[k] * n + n):
                if image[i][j] != num:
                    press += f'({cut(x + dc[k] * n, y + dr[k] * n, n // 2)})'
                    end = 1
                    break
            if end:
                break
        else:
            press += str(num)

    return press


N = int(input().strip())
image = list(list(map(int, input().strip())) for _ in range(N))

dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1]

result = cut(0, 0, N // 2)
if result == '1111':
    result = '1'
elif result == '0000':
    result = '0'
else:
    result = f'({result})'
    
print(result)