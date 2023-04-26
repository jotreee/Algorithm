import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):

    n = int(input().strip())
    sticker = list(list(map(int, input().split())) for _ in range(2))
    if n == 1:
        print(sticker[0][0]) if sticker[0][0] > sticker[1][0] else print(sticker[1][0])

    else:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]

        if n == 2:
            print(sticker[0][1]) if sticker[0][1] > sticker[1][1] else print(sticker[1][1])
        else:
            for i in range(2, n):
                if sticker[0][i - 1] > sticker[0][i - 2]:
                    sticker[1][i] += sticker[0][i - 1]
                else:
                    sticker[1][i] += sticker[0][i - 2]
                if sticker[1][i - 1] > sticker[1][i - 2]:
                    sticker[0][i] += sticker[1][i - 1]
                else:
                    sticker[0][i] += sticker[1][i - 2]
                    
            print(max(sticker[-1] + sticker[-2]))