n = int(input())
a = list(map(int, input().split()))

dic = {a[0] : 0}
b = [-1]
for i in range(1, n):
    if (a[i] in dic):
        b.append(dic[a[i]] + 1)
        dic[a[i]] = i
    else:
        b.append(-1)
        dic[a[i]] = i
print(*b)
