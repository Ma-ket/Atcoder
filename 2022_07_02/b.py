# input
n = int(input())
a = []
for i in range(n):
    a.append(input())  # 文字列

# 処理
def direction(dir1, dir2):
    if(dir1 < 0):
        dir1 = n - dir1
    elif(dir1 >= n):
        dir1 = dir1 - n
    elif(dir2 < 0):
        dir2 = n - dir2
    elif(dir2 >= n):
        dir2 = dir2 - n
    return (dir1, dir2)

max = 0
stn = []
for i in range(n):
    for j in range(n):
        value = int(a[i][j])
        if(max < value):
            max = value
for i in range(n):
    for j in range(n):
        value = int(a[i][j])
        if(value == max):
            stn.append((i, j))
max_val = [max]
for _ in range(n - 1):
    for i in {-1, 0, 1}:
        for j in {-1, 0, 1}:
            dir = direction(stn[0] - i, stn[1] - j)
            value = int(a[dir[0]][dir[1]])
            if(max_val < value):
                max_val.append(value)

