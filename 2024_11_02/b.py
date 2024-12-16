def f(a, b):
    if (a % b == 0):
        return 0
    return 1

n = int(input())
q = {}
r = {}
for i in range(1, n+1):
    q_tmp, r_tmp = map(int, input().split())
    q[i] = q_tmp
    r[i] = r_tmp
m = int(input())
for _ in range(m):
    t, d = map(int, input().split())
    if (d <= r[t]):
        print(r[t])
    else:
        dd = d - r[t]
        div = dd // q[t] + f(dd, q[t])
        print(r[t] + q[t] * div)


