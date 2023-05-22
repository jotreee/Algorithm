import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

dp = [A[0]]
for i in range(1, N):
    if A[i] > dp[-1]:
        dp.append(A[i])
    elif A[i] < dp[0]:
        dp[0] = A[i]
    elif A[i] == dp[-1] or A[i] == dp[0]:
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
                    break
                else:
                    n = (n // 2 if n // 2 > 1 else 1)
                    idx -= n
            else:
                if A[i] < dp[idx + 1]:
                    dp[idx + 1] = A[i]
                    break
                else:
                    n = (n // 2 if n // 2 > 1 else 1)
                    idx += n

print(len(dp))