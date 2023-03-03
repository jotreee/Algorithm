import sys

input = sys.stdin.readline

N, M = map(int, input().split())
note = dict()

for _ in range(N):
    adr, pwd = input().split()
    note.update({adr: pwd})

for _ in range(M):
    print(note[input().strip()])