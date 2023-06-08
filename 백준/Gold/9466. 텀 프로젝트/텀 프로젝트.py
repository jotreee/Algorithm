import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    choice = [0] + list(map(int, input().split()))
    chosen = [0] * (N + 1)
    result = 0
    for i in range(1, N + 1):
        if not chosen[i]:
            chosen[i] = 2
            group = [i]
            while True:
                n = choice[group[-1]]
                if chosen[n] == 1 or chosen[n] == -1:
                    for m in group:
                        chosen[m] = -1
                    result += len(group)
                    break

                elif chosen[n] == 2:
                    end = 0
                    for j in range(len(group)):
                        if group[j] == n:
                            result += j
                            for k in range(j):
                                chosen[group[k]] = -1
                            for k in range(j, len(group)):
                                chosen[group[k]] = 1
                            end = 1
                            break
                    if end:
                        break
                else:
                    group.append(n)
                    chosen[n] = 2
    print(result)