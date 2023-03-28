A, B = input().split()
A = int("".join(reversed(list(A))))
B = int("".join(reversed(list(B))))
print(max(A, B))