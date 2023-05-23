import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

dp = [A[0]]
result = [0] * N
for i in range(1, N):
    if A[i] > dp[-1]:
        dp.append(A[i])
        result[i] = len(dp) - 1
    elif A[i] < dp[0]:
        dp[0] = A[i]
    elif A[i] == dp[-1]:
        result[i] = len(dp) - 1
    elif A[i] == dp[0]:
        pass
    else:
        n = (len(dp) // 2 if len(dp) // 2 > 1 else 1)
        idx = n
        while True:
            if A[i] == dp[idx]:
                break
            elif A[i] < dp[idx]:
                if A[i] > dp[idx - 1]:
                    dp[idx] = A[i]
                    result[i] = idx
                    break
                else:
                    n = (n // 2 if n // 2 > 1 else 1)
                    idx -= n
            else:
                if A[i] < dp[idx + 1]:
                    dp[idx + 1] = A[i]
                    result[i] = idx + 1
                    break
                else:
                    n = (n // 2 if n // 2 > 1 else 1)
                    idx += n

answer = []
n = len(dp) - 1
for i in range(N - 1, -1, -1):
    if result[i] == n:
        answer.append(A[i])
        n -= 1
answer.reverse()
print(len(dp))
print(" ".join(map(str, answer)))