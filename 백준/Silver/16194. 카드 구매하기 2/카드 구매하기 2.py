import sys

input = sys.stdin.readline

N = int(input().strip())
cards = list(map(int, input().split()))
for i in range(1, N):
    for j in range(i if i % 2 else i - 1):
        if cards[j] + cards[i - j - 1] < cards[i]:
            cards[i] = cards[j] + cards[i - j - 1]

print(cards[N - 1])