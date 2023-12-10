n = int(input())
a = list(map(int, input().split()))

value_index = []
for i in range(n):
    tup = (a[i], i)
    value_index += [tup]
value_index.sort(reverse=True)

sum = 0
tups = []
for k in range(n):
    ai, i = value_index[k]
    tups += [(i, sum)]
    sum += ai
tups.sort()
print(tups)

ans = []
for tup in tups:
    a, b = tup
    ans += [b]
print(*ans)
