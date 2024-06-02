n, l, r = map(int, input().split())

a = []
for i in range(1, 1 + n):
    a.append(i)

b = a[l-1:r]
a[l-1:r] = reversed(b)

print(*a)
