from collections import deque

def cal(i, total): # 현재 위치, 현재까지 금액
    global result
    if i + 1 > N:
        result.append(total)
        return
    cal(i + 1, total)
    if i + arr[i][0] > N:
        result.append(total)
    else:
        cal(i + arr[i][0], total + arr[i][1])

N = int(input())
arr = deque(deque(map(int, input().split())) for _ in range(N))
result = deque([])
cal(0, 0)
print(max(result))