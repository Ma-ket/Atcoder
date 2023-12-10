M, D = map(int, input().split())
y, m, d = map(int, input().split())

# 次の日は何日か

if ((d := d + 1) > D):
    d = d - D
    if ((m := m + 1) > M):
        m = m - M
        y += 1

print(*[y, m, d])


