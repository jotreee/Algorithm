def solution(n):
    n = list(map(int, str(n)))
    n.sort()
    n.reverse()
    return int("".join(map(str, n)))