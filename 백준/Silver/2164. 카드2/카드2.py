import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
cards = deque()
for n in range(1, N + 1):
    cards.append(n)

while True:
    if len(cards) == 1:
        print(cards[0])
        break
    cards.popleft()
    if len(cards) == 1:
        print(cards[0])
        break
    cards.append(cards.popleft())