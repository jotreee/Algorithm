string = list(input())
for i in range(len(string)):
    string[i] = (chr(ord(string[i]) + 32) if 65 <= ord(string[i]) < 91 else chr(ord(string[i]) - 32))
print("".join(string))