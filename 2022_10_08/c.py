n = int(input())
a = list(map(int, input().split()))
a.sort(key=None, reverse=True)

odd = 0
even = 0
for i in range(n):
    if(even == 0 and a[i] & 1 == 0):
        for j in range(i+1, n):
            if(a[j] & 1 == 0):
                even = a[i] + a[j]
                break
    elif(odd == 0 and a[i] & 1 == 1):
        for j in range(i+1, n):
            if (a[j] & 1 == 1):
                odd = a[i] + a[j]
                break
if(odd > 0 or even > 0):
    print(max(odd, even))
else:
    print(-1)
