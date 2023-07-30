result = 0
for _ in range(5):
    score = int(input())
    result += (score if score > 40 else 40)
print(result // 5)