import sys

input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))

prime = 0
for num in nums:
    if num == 1:
        continue
    elif num == 2 or num == 3:
        prime += 1
    elif num >= 5:
        for n in range(2, int(num ** 0.5) + 2):
            if not num % n:
                break
        else:
            prime += 1

print(prime)