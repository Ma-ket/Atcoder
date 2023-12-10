n, m = map(int, input().split())
s = input()

ts = m
have_logo = 0
buy_logo = 0
i = 0
while (i < n):
    plan = int(s[i])
    if (plan == 0):
        ts = m
        have_logo = buy_logo
    elif (plan == 1):
        if (ts == 0):
            if (have_logo > 0):
                have_logo -= 1
            else:
                buy_logo += 1
                have_logo += 1
            have_logo -= 1
        else:
            ts -= 1
    elif (plan == 2):
        if (have_logo == 0):
            buy_logo += 1
            have_logo += 1
        have_logo -= 1
    i += 1
    # print(f"{plan}: ts{ts}, logo_b{buy_logo} h{have_logo}")
print(buy_logo)

