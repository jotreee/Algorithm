N = int(input())
star = ["*"] * N
for i in range(N):
    print("".join(star))
    star[i] = " "