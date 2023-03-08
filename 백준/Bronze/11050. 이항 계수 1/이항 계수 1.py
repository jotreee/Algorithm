N, K = map(int, input().split())
K = min(K, N - K)

num1 = 1
for i in range(N - K + 1, N + 1):
    num1 *= i
num2 = 1
for i in range(2, K + 1):
    num2 *= i

print(num1 // num2)