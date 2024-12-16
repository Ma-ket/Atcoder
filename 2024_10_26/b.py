n = 8
masu_i = []
for _ in range(n):
    s = list(input())
    masu_i.append(s)

cnt_i = 0
for i in range(n):
    s = masu_i[i]
    if ('#' not in s):
        cnt_i += 1

cnt_j = 0
for j in range(n):
    s = []
    for i in range(n):
        s.append(masu_i[i][j])
    if ('#' not in s):
        cnt_j += 1

print(cnt_i * cnt_j)
