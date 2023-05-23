import sys

input = sys.stdin.readline


def move(i, j, cnt, visited):
    global result
    for k in range(4):
        if 0 <= i + dr[k] < R and 0 <= j + dc[k] < C and not visited[board[i + dr[k]][j + dc[k]]]:
            visited[board[i + dr[k]][j + dc[k]]] = 1
            move(i + dr[k], j + dc[k], cnt + 1, visited)
            visited[board[i + dr[k]][j + dc[k]]] = 0
    else:
        if cnt > result:
            result = cnt
        return


R, C = map(int, input().split())
board = list(list(input().strip()) for _ in range(R))
for i in range(R):
    for j in range(C):
        board[i][j] = ord(board[i][j]) - 65

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

visit = [0] * 26
visit[board[0][0]] = 1
result = 1
move(0, 0, 1, visit)
print(result)