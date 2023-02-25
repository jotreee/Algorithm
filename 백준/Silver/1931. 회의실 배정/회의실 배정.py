import sys

input = sys.stdin.readline

N = int(input().strip())
meeting = list(list(map(int, input().split())) for _ in range(N))
meeting.sort(key = lambda x: (x[1], x[0]))

end = 0
num = 0

for i in range(N):
    if meeting[i][0] >= end:
        num += 1
        end = meeting[i][1]

print(num)