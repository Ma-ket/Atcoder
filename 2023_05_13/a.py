n = int(input())
s = input()

a = t = 0
if (n % 2 == 0):
    for str in s:
        if (str == "A"):
            a += 1
        else:
            t += 1
        if (a >= n / 2):
            print("A")
            break
        elif (t >= n / 2):
            print("T")
            break
else:
    for str in s:
        if (str == "A"):
            a += 1
        else:
            t += 1
    if (a > t):
        print("A")
    else:
        print("T")
