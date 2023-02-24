import sys
from collections import deque

input = sys.stdin.readline

cards = [0] * (10 ** 7 * 2 + 1)
result = deque()

N = int(input().strip())
arr = deque(map(int, input().split()))

for n in arr:
    cards[n] = 1

M = int(input().strip())
arr = deque(map(int, input().split()))

for n in arr:
  if cards[n]:
      result.append('1')
  else:
      result.append('0')

print(' '.join(result))