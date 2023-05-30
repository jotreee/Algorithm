def solution(s):
    s = list(s)
    if 97 <= ord(s[0]) < 123:
        s[0] = chr(ord(s[0]) - 32)
    for i in range(1, len(s)):
        if s[i - 1] == ' ' and 97 <= ord(s[i]) < 123:
            s[i] = chr(ord(s[i]) - 32)
        elif s[i - 1] != ' ' and 65 <= ord(s[i]) < 91:
            s[i] = chr(ord(s[i]) + 32)
    answer = ''.join(s)
    return answer