import sys

input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))

palindrome = list([0] * N for _ in range(N))

for i in reversed(range(N - 1)):
    for j in range(i + 1, N):
        if palindrome[i + 1][j - 1] >= 0 and nums[i] == nums[j]:
            palindrome[i][j] = 1
        else:
            palindrome[i][j] = -1

M = int(input().strip())
for _ in range(M):
    S, E = map(int, input().split())
    S -= 1
    E -= 1
    print(1 if (palindrome[S][E] == 1 or S == E) else 0)