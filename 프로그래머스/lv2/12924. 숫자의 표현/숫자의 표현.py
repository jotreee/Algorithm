def solution(n):
    answer = 1
    for i in range(1, int(n // 2) + 1):
        s = i
        for j in range(i + 1, n):
            s += j
            if s >= n:
                if s == n:
                    answer += 1
                break
    return answer