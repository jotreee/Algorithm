def solution(s):
    answer = True
    p, y = 0, 0
    for a in s:
        if a == 'p' or a == 'P':
            p += 1
        elif a == 'y' or a == 'Y':
            y += 1
    if p != y:
        answer = False
    return answer