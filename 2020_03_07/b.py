[n, a, b] = list(map(int, input().split()))

ans = 0
quo = n // (a + b)
extra = n - quo * (a + b)

if (extra > 0):  # !=
    if (extra >= a):
        ans = a * quo + a
    else :
        ans = a * quo + extra
else :
    ans = a * quo
print(ans)
