n, k = map(int, input().split())
s = list(input())

cnt = 0
for i in range(n-k+1):
    if ('X' not in s[i:i+k]):
        cnt += 1
        s[i:i+k] = ['X'] * k
print(cnt)
