import sys

input = sys.stdin.readline

N, M = map(int, input().split())
seq = list([[], []] for _ in range(N + 1))
for _ in range(M):
    a, b = map(int, input().split())
    seq[a][1].append(b)
    seq[b][0].append(a)

result = []
nums = list(range(1, N + 1))
while True:
    if nums:
        for n in nums:
            if not seq[n][0]:
                result.append(n)
                nums.remove(n)
                for i in seq[n][1]:
                    seq[i][0].remove(n)
                break
    else:
        print(" ".join(map(str, result)))
        break