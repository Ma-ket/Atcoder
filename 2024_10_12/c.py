n = int(input())
a = []
for i in range(n):
    a.append(list(input()))

def ope(i):
    to = n - i
    y = 0
    for line_list in a:
        if (not (i <= y and y <= to)):
            continue
        print(to, y)
        if(y == to - 1):
            output(a)
        print(a[i:to][y], '\n', list(reversed(line_list[i:to])))
        a[i:to][y] = list(reversed(line_list[i:to]))
        print(a[i:to][y], '\n', list(reversed(line_list[i:to])))
        y += 1

def output(square):
    for line_list in square:
        print("".join(line_list))

for i in range(n//2+1):
    ope(i)
output(a)






