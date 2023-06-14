students = [0] * 30
for _ in range(28):
    students[int(input()) - 1] = 1
for i in range(30):
    if not students[i]:
        print(i + 1)