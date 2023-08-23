arr = [0, 1, 0, 0]
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    arr[a], arr[b] = arr[b], arr[a]
    
for i in range(4):
    if arr[i]:
        print(i)
        break