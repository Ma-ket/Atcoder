n, s, k = map(int, input().split())

i = 0
value = 0
while (i < n):
    p, q = map(int, input().split())
    value += p * q
    i += 1

if (value < s):
    print(value + k)
else:
    print(value)
