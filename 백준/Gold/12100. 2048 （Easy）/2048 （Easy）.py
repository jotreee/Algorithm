import sys, copy

input = sys.stdin.readline


def up(n, board, s):
    global result
    if not n:
        for i in range(N):
            for j in range(N):
                if board[i][j] > result:
                    result = board[i][j]
        return

    merged = list(list([0] * N) for _ in range(N))
    for i in range(1, N):
        for j in range(N):
            for k in range(i):
                if board[i - k - 1][j]:
                    if not merged[i - k - 1][j] and board[i - k - 1][j] == board[i - k][j]:
                        board[i - k - 1][j] *= 2
                        board[i - k][j] = 0
                        merged[i - k - 1][j] = 1
                    break
                board[i - k - 1][j] = board[i - k][j]
                board[i - k][j] = 0

    up(n - 1, copy.deepcopy(board), s + ['u'])
    down(n - 1, copy.deepcopy(board), s + ['d'])
    left(n - 1, copy.deepcopy(board), s + ['l'])
    right(n - 1, copy.deepcopy(board), s + ['r'])


def down(n, board, s):
    global result
    if not n:
        for i in range(N):
            for j in range(N):
                if board[i][j] > result:
                    result = board[i][j]
        return

    merged = list(list([0] * N) for _ in range(N))
    for i in range(N - 2, -1, -1):
        for j in range(N):
            for k in range(N - i - 1):
                if board[i + k + 1][j]:
                    if not merged[i + k + 1][j] and board[i + k + 1][j] == board[i + k][j]:
                        board[i + k + 1][j] *= 2
                        board[i + k][j] = 0
                        merged[i + k + 1][j] = 1
                    break
                board[i + k + 1][j] = board[i + k][j]
                board[i + k][j] = 0

    up(n - 1, copy.deepcopy(board), s + ['u'])
    down(n - 1, copy.deepcopy(board), s + ['d'])
    left(n - 1, copy.deepcopy(board), s + ['l'])
    right(n - 1, copy.deepcopy(board), s + ['r'])


def left(n, board, s):
    global result
    if not n:
        for i in range(N):
            for j in range(N):
                if board[i][j] > result:
                    result = board[i][j]
        return

    merged = list(list([0] * N) for _ in range(N))
    for i in range(N):
        for j in range(1, N):
            for k in range(j):
                if board[i][j - k - 1]:
                    if not merged[i][j - k - 1] and board[i][j - k - 1] == board[i][j - k]:
                        board[i][j - k - 1] *= 2
                        board[i][j - k] = 0
                        merged[i][j - k - 1] = 1
                    break
                board[i][j - k - 1] = board[i][j - k]
                board[i][j - k] = 0

    up(n - 1, copy.deepcopy(board), s + ['u'])
    down(n - 1, copy.deepcopy(board), s + ['d'])
    left(n - 1, copy.deepcopy(board), s + ['l'])
    right(n - 1, copy.deepcopy(board), s + ['r'])


def right(n, board, s):
    global result
    if not n:
        for i in range(N):
            for j in range(N):
                if board[i][j] > result:
                    result = board[i][j]
        return

    merged = list(list([0] * N) for _ in range(N))
    for i in range(N):
        for j in range(N - 2, -1, -1):
            for k in range(N - j - 1):
                if board[i][j + k + 1]:
                    if not merged[i][j + k + 1] and board[i][j + k + 1] == board[i][j + k]:
                        board[i][j + k + 1] *= 2
                        board[i][j + k] = 0
                        merged[i][j + k + 1] = 1
                    break
                board[i][j + k + 1] = board[i][j + k]
                board[i][j + k] = 0

    up(n - 1, copy.deepcopy(board), s + ['u'])
    down(n - 1, copy.deepcopy(board), s + ['d'])
    left(n - 1, copy.deepcopy(board), s + ['l'])
    right(n - 1, copy.deepcopy(board), s + ['r'])


N = int(input().strip())
board = list(list(map(int, input().split())) for _ in range(N))
result = 0
up(5, copy.deepcopy(board), ['u'])
down(5, copy.deepcopy(board), ['d'])
left(5, copy.deepcopy(board), ['l'])
right(5, copy.deepcopy(board), ['r'])
print(result)