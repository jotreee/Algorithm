import sys

input = sys.stdin.readline

N = int(input().strip())
liquid = list(map(int, input().split()))
visited = [0] * N
visited[0], visited[-1] = 1, 1

i, j = 0, N - 1
best = [2000000000, 0, 0]
while True:
    mix = liquid[i] + liquid[j]
    if not mix:
        print(liquid[i], liquid[j])
        break
    if abs(mix) < best[0]:
        best = [abs(mix), i, j]
    if mix < 0 and not visited[i + 1]:
        i += 1
        visited[i] = 1
    elif mix > 0 and not visited[j - 1]:
        j -= 1
        visited[j] = 1
    else:
        print(liquid[best[1]], liquid[best[2]])
        break