n, c = map(int, input().split())
t = list(map(int, list(input().split())))

cnt = 1
recieve_time = t[0]
for i in range(1, n):
    if (t[i] - recieve_time < c):
        pass
    else:
        cnt += 1
        recieve_time = t[i]
print(cnt)
