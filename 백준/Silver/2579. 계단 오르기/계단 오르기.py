N = int(input())
arr = list(int(input()) for _ in range(N))
Sum = [[0] * 2 for _ in range(N)]
Sum[0][0] = Sum[0][1] = arr[0]

if len(arr) > 1:
    Sum[1][0] = arr[1]
    Sum[1][1] = arr[0] + arr[1]

if len(arr) > 2:
    for i in range(2, N):
        Sum[i][0] = max(Sum[i - 2][0], Sum[i - 2][1]) + arr[i]
        Sum[i][1] = Sum[i - 1][0] + arr[i]
        
print(max(Sum[N - 1]))