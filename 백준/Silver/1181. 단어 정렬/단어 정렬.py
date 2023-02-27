import sys

input = sys.stdin.readline

N = int(input().strip())
words = list(input().strip() for _ in range(N))
words = list(set(words))

for i in range(len(words)):
    words[i] = [len(words[i]), words[i]]

words.sort()
for i in range(len(words)):
    print(words[i][1])