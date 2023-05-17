import sys

input = sys.stdin.readline

N = int(input().strip())
liquid = list(map(int, input().split()))
liquid.sort()

best = [3000000000, 0, 0, 0]
for k in reversed(range(2, N)):
    visited = [0] * N
    visited[0], visited[k - 1] = 1, 1
    m_best = [3000000000, 0, 0, 0]
    zero = 0
    i, j = 0, k - 1
    while True:
        mix = liquid[i] + liquid[j] + liquid[k]
        if not mix:
            m_best = [0, i, j, k]
            zero = 1
            break
        elif abs(mix) < m_best[0]:
            m_best = [abs(mix), i, j, k]
        if mix < 0 and not visited[i + 1]:
            i += 1
            visited[i] = 1
        elif mix > 0 and not visited[j - 1]:
            j -= 1
            visited[j] = 1
        else:
            break
    if m_best[0] < best[0]:
        best = m_best
    if liquid[k] < 0 or zero:
        break

print(liquid[best[1]], liquid[best[2]], liquid[best[3]])