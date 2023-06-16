import sys

input = sys.stdin.readline

N = int(input().strip())
arr = [[0, 0]] + list([i + 1, int(input().strip())] for i in range(N))
ox = [0] * (N + 1)
result = []

for i in range(1, N + 1):
    if not ox[i]:
        cycle = [i]
        while True:
            ox[i] = 2
            i = arr[i][1]
            if ox[i] == 1:
                for n in cycle:
                    ox[n] = 0
                break
            elif ox[i] == 2:
                c = 0
                for n in cycle:
                    if n == i:
                        c = 1
                    if c:
                        ox[n] = 1
                        result.append(n)
                    else:
                        ox[n] = 0
                break
            cycle.append(i)

result.sort()
print(len(result))
for n in result:
    print(n)