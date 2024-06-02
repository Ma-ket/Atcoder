n, m = map(int, input().split())

a = list(map(int, input().split()))
x = []
for i in range(n):
    x_line = list(map(int, input().split()))
    x.append(x_line)

nums = [0] * m
for line in x:
    for i in range(m):
        nums[i] += line[i]

result = True
for i in range(m):
    if (a[i] > nums[i]):
        result = False

if (result):
    print("Yes")
else:
    print("No")
