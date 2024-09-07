s = list(input())
t = list(input())

x = []
n = len(s)
while (s != t):
    x_tmp = []
    s_flag = 0
    for i in range(0, n):
        s_tmp = []
        if (s[i] != t[i]):
            s_tmp = list(s)
            s_tmp[i] = t[i]
            x_tmp.append("".join(s_tmp))
            s_flag = 1
    if (s_flag):
        tmp = min(x_tmp)
        s = list(tmp)
        x.append(tmp)

print(len(x))
for a in x:
    print(a)
