a = list(map(int, input().split()))
cnt = 0
for i in range(4):
    for j in range(i+1, 4):
        if (a[i] == a[j] and a[i] > 0 and a[j] > 0):
            a[i] = 0
            a[j] = 0
            cnt += 1
print(cnt)
