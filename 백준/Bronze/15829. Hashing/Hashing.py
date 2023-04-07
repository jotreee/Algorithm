L = int(input())
string = list(input())

hash = 0
for i in range(L):
    hash += (ord(string[i]) - 96) * 31 ** i

print(hash)