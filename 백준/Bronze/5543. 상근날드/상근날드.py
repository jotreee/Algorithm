burger, beverage = 2000, 2000
for _ in range(3):
    n = int(input())
    burger = (n if n < burger else burger)
for _ in range(2):
    n = int(input())
    beverage = (n if n < beverage else beverage)
print(burger + beverage - 50)