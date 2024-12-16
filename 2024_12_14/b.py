n, r = map(int, input().split())
for i in range(n):
    d, a = map(int, input().split())
    if (d == 1 and 1600 <= r and r <= 2799):
        r += a
    elif (d == 2 and 1200 <= r and r <= 2399):
        r += a
    elif (r < 1200 or 2799 < r):
        break
    # print(f"r = {r}") # debug
print(r)
