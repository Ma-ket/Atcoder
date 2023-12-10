n, s, m, l = map(int, input().split())

ans = 10 ** 5

for i in range(n // 6 + 2):
    for j in range(n // 8 + 2):
        for k in range(n // 12 + 2):
            if (n > i*6 + j*8 + k*12):
                continue
            value = i*s + j*m + k*l
            if (ans > value):
                ans = value

print(ans)
