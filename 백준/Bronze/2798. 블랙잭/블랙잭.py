import sys

input = sys.stdin.readline


def card_sum(idx, cnt, n):
    global result
    if not cnt:
        result.append(n)
        return
    if idx == N:
        return
    card_sum(idx + 1, cnt - 1, n + cards[idx])
    card_sum(idx + 1, cnt, n)


N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = []
card_sum(0, 3, 0)
result.sort()
if result[-1] <= M:
    print(result[-1])
else:
    for i in range(len(result)):
        if result[i] == M:
            print(result[i])
            break
        elif result[i] > M:
            print(result[i - 1])
            break