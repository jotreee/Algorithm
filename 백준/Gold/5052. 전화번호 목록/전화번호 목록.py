import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    numbers = list(list(map(int, input().strip())) for _ in range(n))
    numbers.sort()

    no = 0
    for i in range(n - 1):
        if len(numbers[i]) < len(numbers[i + 1]) and numbers[i][0] == numbers[i + 1][0] and numbers[i][-1] == numbers[i + 1][len(numbers[i]) - 1]:
            for j in range(1, len(numbers[i]) - 1):
                if numbers[i][j] != numbers[i + 1][j]:
                    break
            else:
                print("NO")
                no = 1
                break
        if no:
            break
    if not no:
        print("YES")