(a, b) = (map(int, input().split()))
ans = -1
for x in range(1, 1250):
    A = int(x * 0.08)
    B = int(x * 0.1)
    if (A == a and B == b):
        ans = x
        break

print(ans)
