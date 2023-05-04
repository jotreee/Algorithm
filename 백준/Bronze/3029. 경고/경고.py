now = list(map(int, input().split(':')))
bomb = list(map(int, input().split(':')))
h, m, s = bomb[0] - now[0], bomb[1] - now[1], bomb[2] - now[2]

if s < 0:
    s += 60
    m -= 1
if s < 10:
    s = '0' + str(s)
else:
    s = str(s)

if m < 0:
    m += 60
    h -= 1
if m < 10:
    m = '0' + str(m)
else:
    m = str(m)

if h < 0:
    h += 24
if h < 10:
    h = '0' + str(h)
else:
    h = str(h)

if h == m == s == '00':
    h = '24'
print(":".join([h, m, s]))