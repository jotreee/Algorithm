import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input().strip())
cards = list(int(input().strip()) for _ in range(N))
cards.sort()

if N == 1:
    print(0)

else:
    result = 0
    while True:
        if len(cards) == 2:
            print(result + sum(cards))
            break

        a, b = heappop(cards), heappop(cards)
        result += (a + b)
        heappush(cards, a + b)