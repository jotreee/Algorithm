def solution(s):
    stack = 0
    for n in s:
        if n == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
            break
    else:
        if stack:
            return False
        return True