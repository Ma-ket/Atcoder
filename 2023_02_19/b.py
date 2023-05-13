n, k = map(int, input().split())
s = list(input())

t = s
count = 0
for i in range(n):
    if (s[i] == "o"):
        if (count < k):
            count += 1
        else :
            t[i] = "x"
print("".join(t))

