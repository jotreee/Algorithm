n = int(input())
car = list(map(int, input().split()))
result = 0
for c in car:
    if n == c:
        result += 1
print(result)