import sys

input = sys.stdin.readline

T = int(input().strip())
for tc in range(T):
    N = int(input())
    nums = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90

    if N > 10:
        for i in range(11, N + 1):
            nums[i] = nums[i - 5] + nums[i - 1]

    print(nums[N])