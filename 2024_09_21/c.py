n, q = map(int, input().split(" "))
s = input()
x = {}
c = {}
for i in range(q):
    x[i], c[i] = input().split()
    x[i] = int(x[i]) - 1

cnt = len(s.split("ABC")) - 1
s = list(s)

for i in range(q):
    for j in range(3):
        idx = x[i] - j
        if (0 <= idx and idx < n - 2):
            if (s[idx] == 'A' and s[idx + 1] == 'B' and s[idx + 2] == 'C'):
                cnt -= 1
    s[x[i]] = c[i]
    for j in range(3):
        idx = x[i] - j
        if (0 <= idx and idx < n - 2):
            if (s[idx] == 'A' and s[idx + 1] == 'B' and s[idx + 2] == 'C'):
                cnt += 1
    print(cnt)
