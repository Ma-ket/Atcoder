n, m = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))

dic = {}
for i in range(m):
    dic[x[i]] = a[i]
x.sort()

sum_val = 0
sum_idx = 0
for i in range(m):
    if (sum_val < x[i] - 1):
        sum_val = -1
        break
    sum_val += dic[x[i]]
    sum_idx += dic[x[i]] * x[i]

if (sum_val != n or sum_val == -1):
    print("-1")
else:
    print(sum_idx)
