n, k = map(int, input().split())
unlike = list(map(int, input().split()))

like = []
for i in range(0, 10):
    if (i not in unlike):
        like.append(i)

output = 0
for num in range(n, 10 * n):
    digits = list(str(num))
    flag = True
    for digit in digits:
        if (int(digit) in unlike):
            flag = False
    if (flag == True):
        output = num
        break

print(output)
