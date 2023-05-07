grade = input()
n = 0.0
if grade == 'F':
    print(n)
else:
    if grade[0] == 'A':
        n += 4
    elif grade[0] == 'B':
        n += 3
    elif grade[0] == 'C':
        n += 2
    else:
        n += 1

    if grade[1] == '+':
        n += 0.3
    elif grade[1] == '-':
        n -= 0.3
    
    print(n)