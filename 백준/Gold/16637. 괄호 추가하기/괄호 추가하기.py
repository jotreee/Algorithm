n = int(input())
num_str = input().strip()
visit = [0] * (n + 1)    
li = []
max_num = -9999999999999999999999999
if n == 1:
    max_num = int(num_str[0])
 
def result(li1):
    number = int(li1[0])
 
    for i in range(1, len(li1) - 1, 2):
        if li1[i] == '+':
            number += int(li1[i + 1])
        elif li1[i] == '-':
            number -= int(li1[i + 1])
        else:
            number *= int(li1[i + 1])
 
    return number
 
def first_cal(f_li):
    arr = []
    i = 0
 
    while i < len(num_str):
 
        if i in f_li:
            a = arr.pop()
            if num_str[i] == '+':
                num = int(a) + int(num_str[i + 1])
                arr.append(str(num))
                i += 2
            elif num_str[i] == '*':
                num = int(a) * int(num_str[i + 1])
                arr.append(str(num))
                i += 2
            elif num_str[i] == '-':
                num = int(a) - int(num_str[i + 1])
                arr.append(str(num))
                i += 2
        else:
            arr.append(num_str[i])
            i += 1
    return result(arr)
 
 
def calculate(x):
    global max_num
    if len(li) > 0:
 
        r = first_cal(li)
        if max_num < r:
            max_num = r
 
    if x == n:
        return
 
    for i in range(x, n, 2):
 
        if visit[i] == 1:
            continue
        visit[i] = visit[i + 2] = 1
        li.append(i)
        calculate(i + 4)
        li.pop()
        visit[i] = visit[i + 2] = 0
 
 
calculate(1)
print(max_num)