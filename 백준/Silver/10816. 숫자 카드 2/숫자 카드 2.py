import sys

input = sys.stdin.readline

N = int(input().strip())
cards = list(map(int, input().split()))
M = int(input().strip())
problems = list(map(int, input().split()))

result = [0] * 20000001
for i in range(N):
    result[cards[i]] += 1
for i in range(M):
    problems[i] = result[problems[i]]

print(" ".join(map(str, problems)))