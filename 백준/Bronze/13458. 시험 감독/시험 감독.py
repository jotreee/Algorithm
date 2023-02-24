N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0
for people in arr:
    people -= B
    total += 1
    if people > 0:
        if people % C == 0:
            total += (people // C)
        else:
            total += (people // C + 1)

print(total)