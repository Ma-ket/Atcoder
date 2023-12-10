n = int(input())
a = list(map(int, input().split()))

b = {}
for i in set(a):
    b[i] = sum([j for j in a if(j > i)])
# print(b)

ans = a


for i in range(n):
    c = b[a[i]]
    if (i == n - 1):
        print(c)
    else:
        print(c, end=" ")

