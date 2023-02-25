import sys

input = sys.stdin.readline

T = int(input().strip())
for tc in range(T):
    
    N = int(input().strip())
    clothes = dict()
    
    for _ in range(N):
        A, B = input().split()
        if B in clothes:
            for w in clothes[B]:
                if w == A:
                    break
            else:
                clothes[B].append(A)
        else:
            clothes.update({B : [A]})

    result = 1
    for key in clothes:
        result *= (len(clothes[key]) + 1)
    print(result - 1)