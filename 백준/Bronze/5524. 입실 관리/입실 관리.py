N = int(input())
for _ in range(N):
    name = list(input())
    for i in range(len(name)):
        if ord(name[i]) < 97:
            name[i] = chr(ord(name[i]) + 32)
    print("".join(name))