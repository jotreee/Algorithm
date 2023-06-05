import sys

input = sys.stdin.readline

N = int(input().strip())
cards = list(map(int, input().split()))
card_num = [0] * 1000001
for i in range(N):
    card_num[cards[i]] = i + 1
scores = [0] * N

for i in range(N):
    for d in range(1, int(cards[i] ** 0.5) + 1):
        if (cards[i] // d) * d == cards[i]:
            if card_num[d]:
                scores[i] -= 1
                scores[card_num[d] - 1] += 1
            if d != cards[i] // d and card_num[cards[i] // d]:
                scores[i] -= 1
                scores[card_num[cards[i] // d] - 1] += 1

print(" ".join(map(str, scores)))