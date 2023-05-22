import sys

input = sys.stdin.readline


def combi(n, cnt, lst):
    global result
    if cnt == K:
        m = 0
        for i in range(N):
            for j in range(26):
                if j != 0 and j != 2 and j != 8 and j != 13 and j != 19 and ox[i][j]:
                    for k in lst:
                        if alpha[k][1] == j:
                            break
                    else:
                        break
            else:
                m += 1
        if m > result:
            result = m
        return

    for i in range(n + 1, len(alpha) - K + cnt + 1):
        combi(i, cnt + 1, lst + [i])


N, K = map(int, input().split())
if K < 5:
    print(0)
else:
    ox = list([0] * 26 for _ in range(N))
    alpha = list([0, i] for i in range(26))
    for i in range(N):
        for s in ['a', 'c', 'i', 't', 'n']:
            ox[i][ord(s) - 97] = 1
        word = list(input().strip())
        for j in range(4, len(word) - 4):
            if not ox[i][ord(word[j]) - 97]:
                ox[i][ord(word[j]) - 97] = 1
                alpha[ord(word[j]) - 97][0] += 1
    alpha.sort()
    alpha.reverse()
    idx = 25
    for i in range(26):
        if not alpha[i][0]:
            idx = i
            break
    K -= 5
    alpha = alpha[:idx]
    if len(alpha) < K:
        print(N)
    else:
        result = 0
        combi(-1, 0, [])
        print(result)