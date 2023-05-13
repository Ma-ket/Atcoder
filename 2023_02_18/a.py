t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, list(input())))
    s_string = "".join(list(map(str, s)))

    ope = 0
    k = sum(s)
    if (k % 2 == 1):
        print(-1)
    elif (k == 0):
        print(0)
    elif (k >= 4):
        for i in range(n - 2):
            ope += 1
        print(ope)
    elif (k == 2):
        if ("11" not in s_string):
            print(1)
        else :
            if ("11" in s_string[2:]):
                print(2)
            elif("11" in s_string[:2] and n >= 4):
                print(2)
            else :
                if (n == 4):
                    print(3)

