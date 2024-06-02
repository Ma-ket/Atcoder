n, m, k = map(int, input().split())

a, r = [], []
for _ in range(m):
    l = list(input().split())
    r.append(l.pop(-1))
    a.append(set(map(int, l[1:])))

res = 0
for i in range(1 << n):
    tf = []
    for j in range(n):
        if (i & (1 << j)):
            tf.append(1)
        else:
            tf.append(0)
    jud = 1
    for j in range(m):
        ck = 0
        for p in range(n):
            if (a[j] & {p + 1} and tf[p] == 1):
                ck += 1
        if (ck >= k and r[j] == "x"):
            jud = 0
        if (ck < k and r[j] == "o"):
            jud = 0
    if (jud  == 1):
        res += 1

print(res)




