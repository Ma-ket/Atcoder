n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

point = 0
for i in range(m):
    point += a[b[i] - 1]
print(point)
