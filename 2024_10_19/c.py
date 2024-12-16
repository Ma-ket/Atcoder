n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

# print(f"a:{a}\nb:{b}") # debug

cost = a[-1]
cnt = 0
for i in range(n-1):
    if (a[0] > b[0]):
        cost = a.pop(0)
        cnt += 1
        if (cnt > 1):
            break
    else:
        a.pop(0)
        b.pop(0)

if (cnt > 1 or len(a) > 1):
    cost = -1
print(cost)
