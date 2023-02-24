import sys

input = sys.stdin.readline

N, M = map(int, input().split())
connected = [0] * (N + 1)
node = [0] * (N + 1)
lines = list(list(map(int, input().split())) for _ in range(M))

if M == 0:
    print(N)

else:
    new = 1
    no_line = []
    connect = 0

    while True:
        if new == 1:
            connect += 1
            node = [0] * (N + 1)
            connected[lines[0][0]] = 1
            connected[lines[0][1]] = 1
            node[lines[0][0]] = 1
            node[lines[0][1]] = 1
            new = 0

        for i, j in lines:
            if node[i] == 1:
                connected[j] = 1
                node[j] = 1
            elif node[j] == 1:
                connected[i] = 1
                node[i] = 1
            else:
                no_line.append([i, j])
        if no_line:
            if len(lines) == len(no_line):
                new = 1
            lines = no_line
            no_line = []
        else:
            break

    print(connect + N - sum(connected))