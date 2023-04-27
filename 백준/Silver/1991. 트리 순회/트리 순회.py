import sys

input = sys.stdin.readline


def pre_order(i, s, visited, stack):
    if not visited[i]:
        s += [chr(i + 65)]
        visited[i] = 1
    if tree[i][0] != '.' and not visited[ord(tree[i][0]) - 65]:
        if tree[i][1] != '.' and not visited[ord(tree[i][1]) - 65]:
            pre_order(ord(tree[i][0]) - 65, s, visited, stack + [i])
        else:
            pre_order(ord(tree[i][0]) - 65, s, visited, stack)
    elif tree[i][1] != '.' and not visited[ord(tree[i][1]) - 65]:
        pre_order(ord(tree[i][1]) - 65, s, visited, stack)
    elif stack:
        i = stack.pop()
        pre_order(i, s, visited, stack)
    else:
        print("".join(s))
        return


def in_order(i, s, visited, stack):
    if tree[i][0] != '.' and not visited[ord(tree[i][0]) - 65]:
        in_order(ord(tree[i][0]) - 65, s, visited, stack + [i])
    else:
        s += [chr(i + 65)]
        visited[i] = 1
        if tree[i][1] != '.' and not visited[ord(tree[i][1]) - 65]:
            in_order(ord(tree[i][1]) - 65, s, visited, stack)
        elif stack:
            i = stack.pop()
            in_order(i, s, visited, stack)
        else:
            print("".join(s))
            return


def post_order(i, s, visited, stack):
    if tree[i][0] != '.' and not visited[ord(tree[i][0]) - 65]:
        post_order(ord(tree[i][0]) - 65, s, visited, stack + [i])
    elif tree[i][1] != '.' and not visited[ord(tree[i][1]) - 65]:
        post_order(ord(tree[i][1]) - 65, s, visited, stack + [i])
    elif stack:
        s += [chr(i + 65)]
        visited[i] = 1
        i = stack.pop()
        post_order(i, s, visited, stack)
    else:
        print("".join(s + ['A']))
        return


N = int(input().strip())
tree = list([] for _ in range(N))
for _ in range(N):
    p, c1, c2 = input().split()
    tree[ord(p) - 65] = [c1, c2]

pre_order(0, [], [0] * N, [])
in_order(0, [], [0] * N, [])
post_order(0, [], [0] * N, [])