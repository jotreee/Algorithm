def solution(s):
    answer = list(map(int, s.split()))
    answer.sort()
    return " ".join(map(str, [answer[0], answer[-1]]))